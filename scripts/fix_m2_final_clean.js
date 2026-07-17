import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

async function fixFile(relativePath) {
    const filePath = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', relativePath);
    if (!fs.existsSync(filePath)) return;

    const rows = await new Promise((resolve, reject) => {
        const results = [];
        fs.createReadStream(filePath)
          .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
          .on('data', (data) => results.push(data))
          .on('end', () => resolve(results))
          .on('error', reject);
    });

    let headers = Object.keys(rows[0]);
    let fixed = false;

    rows.forEach((row) => {
        let isRowFixed = false;
        
        ['Prefix', 'Chunk1', 'Chunk2', 'Chunk3', 'Chunk4', 'Suffix', 'Original Example'].forEach(col => {
            if (row[col]) {
                let text = row[col];
                let newText = text.replace(/\[CẦN FIX\]/g, '')
                                  .replace(/đemって/g, '伴って')
                                  .replace(/SNS là/g, 'SNS は')
                                  .replace(/」の時代だとすれば、SNS は/g, '」の時代だとすれば、SNS は') // Just making sure
                                  .replace(/ĩa là "đối diện.*/g, '');
                                  
                // For part_75 broken quotes
                if (newText.includes('妹は"怒って')) {
                     newText = newText.replace(/"/g, '');
                }
                if (newText.includes('来月の"引越しに')) {
                     newText = newText.replace(/"/g, '');
                }

                if (text !== newText) {
                    row[col] = newText;
                    isRowFixed = true;
                    fixed = true;
                }
            }
        });
        
        // Ensure Original Example perfectly matches reconstructed after fixing
        if (isRowFixed) {
            row['Original Example'] = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
        }
    });

    if (fixed) {
        const csvWriter = createObjectCsvWriter({
            path: filePath,
            header: headers.map(h => ({ id: h, title: h }))
        });
        await csvWriter.writeRecords(rows);
    }
}

async function run() {
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled');
  let totalFixed = 0;

  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        await fixFile(path.join(set, file));
      }
    }
  }
}

run().catch(console.error);
