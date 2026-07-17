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
    await fixFile('set_1_daily/part_75.csv', (row, i) => {
        if (i === 8) {
            row['Prefix'] = '来月の';
            row['Chunk1'] = '引越しに';
            row['Chunk2'] = '向けて、';
            row['Chunk3'] = '少しずつ荷物の';
            row['Chunk4'] = '片付けを';
            row['Suffix'] = '始めている。';
            return true;
        }
        return false;
    });

    await fixFile('set_4_literature/part_38.csv', (row, i) => {
        if (i === 15) {
            row['Prefix'] = '「彼、どこへ行ったの？」「どこって、';
            row['Chunk1'] = 'いつもの';
            row['Chunk2'] = '古い';
            row['Chunk3'] = '図書館';
            row['Chunk4'] = 'だよ。';
            row['Suffix'] = '」';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_27.csv', (row, i) => {
        if (i === 10) {
            row['Prefix'] = '今回のドキュメンタリー番組は、';
            row['Chunk1'] = 'せめて';
            row['Chunk2'] = 'ゴールデンタイムに';
            row['Chunk3'] = '放映して';
            row['Chunk4'] = 'ほしかった。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_28.csv', (row, i) => {
        if (i === 1) {
            row['Prefix'] = '老記者は静かにペンを置き、事件の資料をすべて引き出しに仕舞った。';
            row['Chunk1'] = 'そうして、';
            row['Chunk2'] = 'ゆっくりと';
            row['Chunk3'] = '立ち';
            row['Chunk4'] = '上がった。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 7) {
            row['Prefix'] = '法廷に立つ被告は、自分の犯した罪の重さに、';
            row['Chunk1'] = 'いかにも';
            row['Chunk2'] = '悔し';
            row['Chunk3'] = 'そうに';
            row['Chunk4'] = '見えた。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 13) {
            row['Prefix'] = '最新の世論調査の結果を見る限り、';
            row['Chunk1'] = '現政権は';
            row['Chunk2'] = '近く';
            row['Chunk3'] = '退陣';
            row['Chunk4'] = 'しそうだ。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_30.csv', (row, i) => {
        if (i === 9) {
            row['Prefix'] = 'あの雑誌は';
            row['Chunk1'] = '記事の';
            row['Chunk2'] = '内容が浅い。それに';
            row['Chunk3'] = '価格も';
            row['Chunk4'] = '高すぎる。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 16) {
            row['Prefix'] = 'いくら崇高な理想を語っても、';
            row['Chunk1'] = '逮捕されて';
            row['Chunk2'] = 'しまえば';
            row['Chunk3'] = 'それまで';
            row['Chunk4'] = 'だ。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_40.csv', (row, i) => {
        if (i === 2) {
            row['Prefix'] = '彼は重い荷物を抱えて、';
            row['Chunk1'] = '山の';
            row['Chunk2'] = '頂上へ';
            row['Chunk3'] = '歩いて';
            row['Chunk4'] = 'いく。';
            row['Suffix'] = '';
            return true;
        }
        if (i === 11) {
            row['Prefix'] = 'お忙しいところ恐縮ですが、';
            row['Chunk1'] = 'インタビューに';
            row['Chunk2'] = '答えて';
            row['Chunk3'] = 'いただけます';
            row['Chunk4'] = 'か。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_55.csv', (row, i) => {
        if (i === 6) {
            row['Prefix'] = 'この遺跡で発見された土器は、';
            row['Chunk1'] = '古代の';
            row['Chunk2'] = '儀式で';
            row['Chunk3'] = '使われた重要な';
            row['Chunk4'] = '道具とされている。';
            row['Suffix'] = '';
            return true;
        }
        return false;
    });
}

run().catch(console.error);
