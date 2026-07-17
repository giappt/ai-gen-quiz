import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const files = ['part_63.csv', 'part_62.csv', 'part_61.csv', 'part_51.csv', 'part_5.csv'];

files.forEach(f => {
    const filePath = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', 'set_5_jlpt_exam', f);
    if (!fs.existsSync(filePath)) return;

    const rows = [];
    fs.createReadStream(filePath)
        .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
        .on('data', data => rows.push(data))
        .on('end', () => {
            console.log(`[${f}]`);
            rows.forEach((r, i) => {
                console.log(`${i+2}: ${r.Prefix}|${r.Chunk1}|${r.Chunk2}|${r.Chunk3}|${r.Chunk4}|${r.Suffix}`);
            });
        });
});
