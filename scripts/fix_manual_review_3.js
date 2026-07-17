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
    await fixFile('set_5_jlpt_exam/part_87.csv', (row, i) => {
        if (i === 4) { // R6
            row['Prefix'] = '試験で高い点数を取るために、間違えた問題を';
            row['Chunk1'] = '何度も';
            row['Chunk2'] = '復習';
            row['Chunk3'] = 'した';
            row['Chunk4'] = 'ほうがいい。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 9) { // R11
            row['Prefix'] = '物理の試験に合格するためには、公式を';
            row['Chunk1'] = '暗記する';
            row['Chunk2'] = 'ほかに';
            row['Chunk3'] = '過去問を';
            row['Chunk4'] = '解く必要がある。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 15) { // R17
            row['Prefix'] = 'この難解な古典を解読するには、辞書を頼りに';
            row['Chunk1'] = '一字';
            row['Chunk2'] = 'ずつ';
            row['Chunk3'] = '読むよりほかに';
            row['Chunk4'] = '手立てはない。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_86.csv', (row, i) => {
        if (i === 2) { // R4
            row['Prefix'] = '予備調査を徹底して';
            row['Chunk1'] = '行う';
            row['Chunk2'] = 'べきだった';
            row['Chunk3'] = 'と深く';
            row['Chunk4'] = '後悔している。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 8) { // R10
            row['Prefix'] = '留学生のリーさんは日本語の';
            row['Chunk1'] = 'スピーチが';
            row['Chunk2'] = 'へたです';
            row['Chunk3'] = 'が、毎日';
            row['Chunk4'] = '練習します。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 9) { // R11
            row['Prefix'] = '山田さんはみんなの前で';
            row['Chunk1'] = '漢字を';
            row['Chunk2'] = '書く';
            row['Chunk3'] = 'のが';
            row['Chunk4'] = 'へたですから、緊張します。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 19) { // R21
            row['Prefix'] = 'あの教授の';
            row['Chunk1'] = '説明は';
            row['Chunk2'] = '終始理屈っぽくて';
            row['Chunk3'] = '理解する';
            row['Chunk4'] = 'のが難しい。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_82.csv', (row, i) => {
        if (i === 6) { // R8
            row['Prefix'] = 'この論文を完成させるために、';
            row['Chunk1'] = '三日間';
            row['Chunk2'] = 'ばかり';
            row['Chunk3'] = '研究室に';
            row['Chunk4'] = 'こもった。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 8) { // R10
            row['Prefix'] = '彼は試験の前なのに、';
            row['Chunk1'] = '勉強';
            row['Chunk2'] = 'せずに';
            row['Chunk3'] = 'ゲームをして';
            row['Chunk4'] = 'ばかりいる。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 11) { // R13
            row['Prefix'] = '私は先週この大学に';
            row['Chunk1'] = '入学した';
            row['Chunk2'] = 'ばかりで、';
            row['Chunk3'] = '学内の施設が';
            row['Chunk4'] = 'よくわからない。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 17) { // R19
            row['Prefix'] = '第一志望の大学に合格したいばかりに、';
            row['Chunk1'] = '毎日';
            row['Chunk2'] = '必死で';
            row['Chunk3'] = '十時間も';
            row['Chunk4'] = '勉強し続けている。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });
}

run().catch(console.error);
