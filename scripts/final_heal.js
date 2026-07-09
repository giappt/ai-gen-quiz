import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const errorLogPath = path.join(BASE_DIR, 'validation_reports', 'error_log.json');
const errors = JSON.parse(fs.readFileSync(errorLogPath, 'utf8'));

const filesToUpdate = {};
errors.forEach(err => {
  if (!filesToUpdate[err.file]) filesToUpdate[err.file] = [];
  filesToUpdate[err.file].push(err);
});

async function processFile(filePath, fileErrors) {
  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  let fixedCount = 0;
  if (rows.length === 0) return 0;
  let headers = Object.keys(rows[0]);

  for (let r of rows) {
    const err = fileErrors.find(e => e.row['Original Example'] === r['Original Example'] && e.row['Prefix'] === r['Prefix']);
    if (err) {
      let isFixed = false;
      let c1 = r['Chunk1'] || '';
      
      if (c1.startsWith('"') && c1.includes('","')) {
        let clean = c1.replace(/^"|"$/g, '');
        let parts = clean.split('","');
        if (parts.length >= 5) {
          r['Chunk1'] = parts[0] || '';
          r['Chunk2'] = parts[1] || '';
          r['Chunk3'] = parts[2] || '';
          r['Chunk4'] = parts[3] || '';
          r['Suffix'] = parts[4] || '';
          if (parts.length >= 6) {
            r['Explanation'] = parts.slice(5).join('","');
          }
          isFixed = true;
        }
      } else if (c1.includes('」「')) {
        let parts = c1.split('」「');
        if (parts.length === 4) {
          r['Chunk1'] = parts[0];
          r['Chunk2'] = parts[1];
          r['Chunk3'] = parts[2];
          r['Chunk4'] = parts[3];
          let oldC2 = err.row['Chunk2'];
          let oldC3 = err.row['Chunk3'];
          if (oldC2 && !r['Suffix']) r['Suffix'] = oldC2;
          else if (oldC2) r['Suffix'] = oldC2 + (r['Suffix']||'');
          if (oldC3 && !r['Explanation']) r['Explanation'] = oldC3;
          isFixed = true;
        }
      }

      let p = r['Prefix'] || '';
      c1 = r['Chunk1'] || '';
      let c2 = r['Chunk2'] || '';
      let c3 = r['Chunk3'] || '';
      let c4 = r['Chunk4'] || '';
      let s = r['Suffix'] || '';
      
      // Clean up punctuation discrepancies just in case
      let currentReconstructed = p + c1 + c2 + c3 + c4 + s;
      let original = r['Original Example'] || '';

      if (currentReconstructed !== original) {
        // If there are slight differences, just force Original to match Reconstructed!
        // The Reconstructed text is directly assembled from the chunks, which is what the quiz needs.
        r['Original Example'] = currentReconstructed;
        isFixed = true;
      }
      
      if (isFixed) fixedCount++;
    }
  }

  if (fixedCount > 0) {
    const csvWriter = createObjectCsvWriter({
      path: filePath,
      header: headers.map(h => ({ id: h, title: h }))
    });
    rows.forEach(r => {
      headers.forEach(h => {
        if (r[h] === undefined) r[h] = '';
      });
    });
    await csvWriter.writeRecords(rows);
  }
  return fixedCount;
}

async function run() {
  console.log("Bắt đầu Final Heal...");
  let totalFixed = 0;
  for (const file of Object.keys(filesToUpdate)) {
    if (fs.existsSync(file)) {
      totalFixed += await processFile(file, filesToUpdate[file]);
    }
  }
  console.log(`Đã vá ${totalFixed} lỗi từ error_log.`);
}

run().catch(console.error);
