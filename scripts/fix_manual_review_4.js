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
    await fixFile('set_5_jlpt_exam/part_81.csv', (row, i) => {
        if (i === 1) { // R3
            row['Prefix'] = 'あの人は入社してから';
            row['Chunk1'] = 'という';
            row['Chunk2'] = 'もの、';
            row['Chunk3'] = '毎日遅くまで';
            row['Chunk4'] = '残業している。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 9) { // R11
            row['Prefix'] = '人間は誰しも';
            row['Chunk1'] = '失敗';
            row['Chunk2'] = 'から';
            row['Chunk3'] = '学ぶ';
            row['Chunk4'] = 'ものだ。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 14) { // R16
            row['Prefix'] = 'この厳しい財政状況のなか、';
            row['Chunk1'] = '新規事業に';
            row['Chunk2'] = '予算を';
            row['Chunk3'] = '割く';
            row['Chunk4'] = 'など無理な相談だ。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 18) { // R20
            row['Prefix'] = 'もう少し高精度な';
            row['Chunk1'] = '観測データが';
            row['Chunk2'] = 'あれば、';
            row['Chunk3'] = 'この学術的な謎を';
            row['Chunk4'] = '解明できるのだが。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 19) { // R21
            row['Prefix'] = '政府がもっと早く';
            row['Chunk1'] = '経済対策を';
            row['Chunk2'] = '講じて';
            row['Chunk3'] = 'いれば、';
            row['Chunk4'] = '物価の上昇はある程度抑えられたはずだ。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_78.csv', (row, i) => {
        if (i === 11) { // R13
            row['Prefix'] = '大学は';
            row['Chunk1'] = '高度な研究を';
            row['Chunk2'] = '行う';
            row['Chunk3'] = '機関なの';
            row['Chunk4'] = 'だから、受け身の姿勢では意味がない。';
            row['Suffix'] = '';
            // update original example quote marks if broken
            row['Suffix'] = row['Suffix'].replace(/"/g, '');
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_77.csv', (row, i) => {
        if (i === 0) { // R2
            row['Prefix'] = '当該研究機関は、地質変動の影響を';
            row['Chunk1'] = '広範な地域に';
            row['Chunk2'] = 'わたって';
            row['Chunk3'] = '詳細に調査し';
            row['Chunk4'] = '続けた。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 9) { // R11
            row['Prefix'] = '今回の検討会では、抽象的な概念の議論は';
            row['Chunk1'] = 'ぬきに';
            row['Chunk2'] = 'して、';
            row['Chunk3'] = '具体的な数値を';
            row['Chunk4'] = '分析するべきだ。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 14) { // R16
            row['Prefix'] = '私は昨日、大学の図書館の';
            row['Chunk1'] = '古い';
            row['Chunk2'] = '資料を';
            row['Chunk3'] = 'たくさん';
            row['Chunk4'] = '読みました。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });
}

run().catch(console.error);
