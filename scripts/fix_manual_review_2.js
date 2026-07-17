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

    let headers = Object.keys(rows[0]);
    let fixed = false;

    rows.forEach((row, i) => {
        if (updateFn(row, i)) {
            row['Original Example'] = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
            fixed = true;
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
    await fixFile('set_5_jlpt_exam/part_93.csv', (row, i) => {
        if (i === 0) { // R2
            row['Prefix'] = '経営陣は、構造改革に';
            row['Chunk1'] = '多大な';
            row['Chunk2'] = '痛みが';
            row['Chunk3'] = '伴うのを';
            row['Chunk4'] = '見込んで、';
            row['Suffix'] = 'あらかじめ周到な救済策を用意していた。';
            return true;
        }
        if (i === 5) { // R7
            row['Prefix'] = '私は、';
            row['Chunk1'] = '故郷';
            row['Chunk2'] = 'みたいな';
            row['Chunk3'] = '静かな場所に';
            row['Chunk4'] = '住んでみたい。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 9) { // R11
            row['Prefix'] = 'データ分析の結果からすると、この実験は完全に';
            row['Chunk1'] = '計画';
            row['Chunk2'] = '通りに';
            row['Chunk3'] = 'いかなかった';
            row['Chunk4'] = 'みたいだ。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 10) { // R12
            row['Prefix'] = '私は';
            row['Chunk1'] = 'フランス語や';
            row['Chunk2'] = 'イタリア語';
            row['Chunk3'] = 'みたいな';
            row['Chunk4'] = '響きの可愛い言葉を習いたい。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_92.csv', (row, i) => {
        if (i === 0) { // R2
            row['Prefix'] = '試験が始まりますので、まもなく';
            row['Chunk1'] = '解答';
            row['Chunk2'] = '用紙';
            row['Chunk3'] = 'を';
            row['Chunk4'] = '配ります。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_91.csv', (row, i) => {
        if (i === 0) { // R2
            row['Prefix'] = '受験生たちはタクシーに乗らずに試験会場';
            row['Chunk1'] = 'まで';
            row['Chunk2'] = '歩いて';
            row['Chunk3'] = '行く';
            row['Chunk4'] = 'ことにした。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 1) { // R3
            row['Prefix'] = '教授は今日の午後五時';
            row['Chunk1'] = 'まで';
            row['Chunk2'] = '講義を';
            row['Chunk3'] = '継続して';
            row['Chunk4'] = '行います。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 2) { // R4
            row['Prefix'] = '来年の試験に合格する';
            row['Chunk1'] = 'まで、';
            row['Chunk2'] = '毎日';
            row['Chunk3'] = '必死に';
            row['Chunk4'] = '勉強を続けます。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });
}

run().catch(console.error);
