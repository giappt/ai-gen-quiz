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
                let newText = text.replace(/là m/g, 'làm')
                                  .replace(/là \.\.\./g, 'là...')
                                  .replace(/là \)/g, 'là)');
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
    await fixFile('set_2_business/part_10.csv');
    await fixFile('set_2_business/part_100.csv');
    await fixFile('set_2_business/part_87.csv');
    await fixFile('set_2_business/part_94.csv');
}

run().catch(console.error);
