import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

async function fixFile(relativePath, updateFn) {
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

    let fixed = false;
    rows.forEach((row, i) => {
        if (updateFn(row, i + 2)) {
            row['Original Example'] = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
            fixed = true;
        }
    });

    if (fixed) {
        const csvWriter = createObjectCsvWriter({
            path: filePath,
            header: Object.keys(rows[0]).map(h => ({ id: h, title: h }))
        });
        await csvWriter.writeRecords(rows);
        console.log(`Fixed ${relativePath}`);
    }
}

async function run() {
    await fixFile('set_5_jlpt_exam/part_46.csv', (row, i) => {
        let changed = false;
        if (row.Prefix === 'ねえ、私が') { row.Prefix = '「ねえ、私が'; changed = true; }
        if (row.Chunk3 === 'null少し読んで') { row.Chunk3 = '少し読んで'; changed = true; }
        if (row.Suffix === '？と彼女は尋ねた。') { row.Suffix = '？」と彼女は尋ねた。'; changed = true; }
        return changed;
    });

    await fixFile('set_5_jlpt_exam/part_44.csv', (row, i) => {
        let changed = false;
        if (row.Prefix === '主人公は拳を握り締め、必ずnull') { row.Prefix = '主人公は拳を握り締め、「必ず'; changed = true; }
        if (row.Chunk3 === 'element: でも、') { row.Chunk3 = 'でも、'; changed = true; }
        return changed;
    });
}

run().catch(console.error);
