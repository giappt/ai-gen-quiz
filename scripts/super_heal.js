import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const errorLogPath = path.join(BASE_DIR, 'validation_reports', 'error_log.json');
const remainingErrors = [];

async function processFile(filePath) {
  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  if (rows.length === 0) return { fixed: 0, total: 0 };

  let fixedCount = 0;
  let headers = Object.keys(rows[0]);

  rows.forEach(row => {
    let original = (row['Original Example'] || '').trim();
    if (!original) return;
    
    let isFixed = false;

    let p = (row['Prefix'] || '');
    let c1 = (row['Chunk1'] || '');
    let c2 = (row['Chunk2'] || '');
    let c3 = (row['Chunk3'] || '');
    let c4 = (row['Chunk4'] || '');
    let s = (row['Suffix'] || '');
    
    let currentReconstructed = p + c1 + c2 + c3 + c4 + s;

    if (currentReconstructed !== original) {
      // Heuristic 1: Chunk1 contains "」「"
      if (c1.includes('」「')) {
        let parts = c1.split('」「');
        if (parts.length === 4) {
          row['Chunk1'] = parts[0];
          row['Chunk2'] = parts[1];
          row['Chunk3'] = parts[2];
          row['Chunk4'] = parts[3];
          if (c2 && !s) {
            row['Suffix'] = c2;
          } else if (c2) {
             row['Suffix'] = c2 + s;
          }
          if (c3 && !row['Explanation']) {
            row['Explanation'] = c3;
          }
          isFixed = true;
        }
      }

      // Re-evaluate after Heuristic 1
      if (isFixed) {
         p = (row['Prefix'] || '');
         c1 = (row['Chunk1'] || '');
         c2 = (row['Chunk2'] || '');
         c3 = (row['Chunk3'] || '');
         c4 = (row['Chunk4'] || '');
         s = (row['Suffix'] || '');
         currentReconstructed = p + c1 + c2 + c3 + c4 + s;
      }

      if (currentReconstructed !== original) {
        // Heuristic 2: Original Example is junk
        if (original === 'base_text' || original.startsWith('original table row') || original.startsWith('original row')) {
          row['Original Example'] = currentReconstructed;
          isFixed = true;
          original = currentReconstructed;
        }
        
        // Heuristic 3: Furigana in original
        if (!isFixed && original.replace(/（.*?）/g, '') === currentReconstructed) {
          row['Original Example'] = currentReconstructed;
          isFixed = true;
          original = currentReconstructed;
        }

        // Heuristic 4: "của" typo
        if (!isFixed && original.replace(/ của /g, 'の') === currentReconstructed) {
          row['Original Example'] = currentReconstructed;
          isFixed = true;
          original = currentReconstructed;
        }

        // Heuristic 5: missing period in reconstructed
        if (!isFixed && currentReconstructed + '。' === original) {
          row['Suffix'] = s + '。';
          isFixed = true;
          currentReconstructed = p + c1 + c2 + c3 + c4 + row['Suffix'];
        }
        // missing period in reconstructed but original has it with quotes?
        if (!isFixed && currentReconstructed + '。' === original.replace(/"/g, '')) {
           row['Suffix'] = s + '。';
           row['Original Example'] = original.replace(/"/g, '');
           isFixed = true;
           original = row['Original Example'];
           currentReconstructed = p + c1 + c2 + c3 + c4 + row['Suffix'];
        }

        // Heuristic 6: comma difference
        if (!isFixed && currentReconstructed.replace(/,/g, '、') === original) {
          if (p.includes(',')) row['Prefix'] = p.replace(/,/g, '、');
          if (c1.includes(',')) row['Chunk1'] = c1.replace(/,/g, '、');
          if (c2.includes(',')) row['Chunk2'] = c2.replace(/,/g, '、');
          if (c3.includes(',')) row['Chunk3'] = c3.replace(/,/g, '、');
          if (c4.includes(',')) row['Chunk4'] = c4.replace(/,/g, '、');
          if (s.includes(',')) row['Suffix'] = s.replace(/,/g, '、');
          isFixed = true;
          p = (row['Prefix'] || ''); c1 = (row['Chunk1'] || ''); c2 = (row['Chunk2'] || ''); c3 = (row['Chunk3'] || ''); c4 = (row['Chunk4'] || ''); s = (row['Suffix'] || '');
          currentReconstructed = p + c1 + c2 + c3 + c4 + s;
        }

        // Heuristic 7: missing "都会の" or similar small prefix discrepancy, wait let's just use remove spaces check
        if (!isFixed && currentReconstructed.replace(/\s+/g, '') === original.replace(/\s+/g, '')) {
          row['Original Example'] = currentReconstructed;
          isFixed = true;
          original = currentReconstructed;
        }
        
        // Heuristic 8: ' ' instead of '、' or vice versa
        if (!isFixed && currentReconstructed.replace(/[、\s]/g, '') === original.replace(/[、\s]/g, '')) {
          row['Original Example'] = currentReconstructed;
          isFixed = true;
          original = currentReconstructed;
        }
      }

      if (currentReconstructed !== original && !isFixed) {
        remainingErrors.push({
          file: filePath,
          type: 'M2_CHUNK_MISMATCH',
          original: original,
          reconstructed: currentReconstructed,
          row: row
        });
      }
    }
    
    if (isFixed) fixedCount++;
  });

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
  
  return { fixed: fixedCount, total: rows.length };
}

async function run() {
  console.log("Bắt đầu Super Heal...");
  
  let totalM2Fixed = 0;

  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_cleaned');
  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        const stats = await processFile(path.join(m2Dir, set, file));
        totalM2Fixed += stats.fixed;
      }
    }
  }

  const reportsDir = path.join(BASE_DIR, 'validation_reports');
  if (!fs.existsSync(reportsDir)) {
      fs.mkdirSync(reportsDir, { recursive: true });
  }
  fs.writeFileSync(errorLogPath, JSON.stringify(remainingErrors, null, 2), 'utf8');

  console.log(`Đã vá tự động ${totalM2Fixed} lỗi của Mondai 2.`);
  console.log(`Còn lại ${remainingErrors.length} lỗi không thể tự vá. Đã ghi đè vào: ${errorLogPath}`);
}

run().catch(console.error);
