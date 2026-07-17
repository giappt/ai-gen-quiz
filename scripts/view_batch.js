import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const files = ['part_81.csv', 'part_80.csv', 'part_79.csv', 'part_78.csv', 'part_77.csv'];

files.forEach(f => {
    const filePath = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', 'set_5_jlpt_exam', f);
    if (!fs.existsSync(filePath)) return;

    const rows = [];
    fs.createReadStream(filePath)
        .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
        .on('data', data => rows.push(data))
        .on('end', () => {
            console.log(`\n========== ${f} ==========`);
            rows.forEach((r, i) => {
                console.log(`[R${i+2}] P: ${r.Prefix} | C1: ${r.Chunk1} | C2: ${r.Chunk2} | C3: ${r.Chunk3} | C4: ${r.Chunk4} | S: ${r.Suffix}`);
            });
        });
});
