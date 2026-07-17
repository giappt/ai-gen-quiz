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
    await fixFile('set_5_jlpt_exam/part_62.csv', (row, i) => {
        let changed = false;
        if (row.Chunk3 === 'null何度も') { row.Chunk3 = '何度も'; changed = true; }
        if (row.Prefix === '早く真実を') { row.Prefix = '「早く真実を'; changed = true; }
        if (row.Suffix === 'と彼は脅した。' && row.Chunk4 === '通報するぞ') { row.Suffix = '」と彼は脅した。'; changed = true; }
        if (row.Prefix === 'この事件を解決するためには、私が犯人と') { row.Prefix = '「この事件を解決するためには、私が犯人と'; changed = true; }
        if (row.Suffix === 'と彼女は決意した。') { row.Suffix = '」と彼女は決意した。'; changed = true; }
        if (row.Prefix === '今は無理して') { row.Prefix = '「今は無理して'; changed = true; }
        if (row.Suffix === 'ですよと記者は優しく言った。') { row.Suffix = 'ですよ」と記者は優しく言った。'; changed = true; }
        return changed;
    });

    await fixFile('set_5_jlpt_exam/part_61.csv', (row, i) => {
        let changed = false;
        if (row.Chunk3 === '0決定') { row.Chunk3 = '決定'; changed = true; }
        if (row.Prefix === '私の過去を') { row.Prefix = '「私の過去を'; changed = true; }
        if (row.Chunk2 === '0納') { row.Chunk2 = '納'; changed = true; }
        return changed;
    });

    await fixFile('set_5_jlpt_exam/part_51.csv', (row, i) => {
        let changed = false;
        if (row.Prefix === '出版社の') { row.Prefix = '「出版社の'; changed = true; }
        if (row.Prefix === '困難な状況だが、彼女は未来はきっと') { row.Prefix = '困難な状況だが、彼女は「未来はきっと'; changed = true; }
        if (row.Chunk3 === '0どうに') { row.Chunk3 = 'どうに'; changed = true; }
        if (row.Prefix === '最近の若者の') { row.Prefix = '「最近の若者の'; changed = true; }
        if (row.Prefix === '先生、') { row.Prefix = '「先生、'; changed = true; }
        return changed;
    });

    await fixFile('set_5_jlpt_exam/part_5.csv', (row, i) => {
        let changed = false;
        if (row.Prefix === '赤い') { row.Prefix = '「赤い'; changed = true; }
        if (row.Prefix === '以後、') { row.Prefix = '「以後、'; changed = true; }
        if (row.Prefix === '国政の運営において、私的な') { row.Prefix = '「国政の運営において、私的な'; changed = true; }
        return changed;
    });
}

run().catch(console.error);
