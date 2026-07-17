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
    await fixFile('set_5_jlpt_exam/part_75.csv', (row, i) => {
        if (i === 2) {
            row.Prefix = '難関大学の入試を突破するには、';
            row.Chunk1 = '学習計画を'; row.Chunk2 = '根本から'; row.Chunk3 = '見直す'; row.Chunk4 = '必要がある。';
            row.Suffix = ''; return true;
        }
        if (i === 7) {
            row.Prefix = '従来の学界における共通認識に反し、';
            row.Chunk1 = 'この新仮説は'; row.Chunk2 = '正当性が'; row.Chunk3 = '証明'; row.Chunk4 = 'された。';
            row.Suffix = ''; return true;
        }
        if (i === 8) {
            row.Prefix = '研究者たちの当初の仮説に反して、';
            row.Chunk1 = '実験は'; row.Chunk2 = '全く'; row.Chunk3 = '予期せぬ'; row.Chunk4 = '結果をもたらした。';
            row.Suffix = ''; return true;
        }
        if (i === 12) {
            row.Prefix = '観測船は調査データを収集するため、';
            row.Chunk1 = '北極海に'; row.Chunk2 = '向かって'; row.Chunk3 = 'ゆっくりと進んで'; row.Chunk4 = 'いる。';
            row.Suffix = ''; return true;
        }
        if (i === 13) {
            row.Prefix = '受験生は試験中、常に画面に';
            row.Chunk1 = '向かって'; row.Chunk2 = '正しく'; row.Chunk3 = '着席'; row.Chunk4 = 'しなければならない。';
            row.Suffix = ''; return true;
        }
        if (i === 19) {
            row.Prefix = '閑静な敷地内の公園に面して、';
            row.Chunk1 = '近現代的な'; row.Chunk2 = '大学図書館が'; row.Chunk3 = '建設'; row.Chunk4 = 'された。';
            row.Suffix = ''; return true;
        }
        if (i === 20) {
            row.Prefix = '深刻な財政危機に面して、';
            row.Chunk1 = '理事会は'; row.Chunk2 = '抜本的な'; row.Chunk3 = '構造改革を'; row.Chunk4 = '断行せざるを得なかった。';
            row.Suffix = ''; return true;
        }
        if (i === 21) {
            row.Prefix = '提出された論文の結論部分にも、';
            row.Chunk1 = '重大な'; row.Chunk2 = '数値の'; row.Chunk3 = '誤りが'; row.Chunk4 = '発見された。';
            row.Suffix = ''; return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_74.csv', (row, i) => {
        if (i === 4) {
            row.Prefix = '会議では今年度の予算案の修正につき、';
            row.Chunk1 = '多角的な'; row.Chunk2 = '視点'; row.Chunk3 = 'から'; row.Chunk4 = '議論が交わされた。';
            row.Suffix = ''; return true;
        }
        if (i === 5) {
            row.Prefix = 'サーバーの保守点検につき、本日のサービス提供を';
            row.Chunk1 = '一時'; row.Chunk2 = '停止'; row.Chunk3 = 'いたし'; row.Chunk4 = 'ます。';
            row.Suffix = ''; return true;
        }
        if (i === 9) {
            row.Prefix = '政策に賛成するにつけ反対するにつけ、';
            row.Chunk1 = '具体的な'; row.Chunk2 = '根拠を'; row.Chunk3 = '提示しなければ'; row.Chunk4 = '説得力に欠ける。';
            row.Suffix = ''; return true;
        }
        if (i === 13) {
            row.Prefix = '私たちは歴史的悲劇を';
            row.Chunk1 = '二度と'; row.Chunk2 = '繰り返しては'; row.Chunk3 = 'ならないと'; row.Chunk4 = '強く誓う。';
            row.Suffix = ''; return true;
        }
        if (i === 18) {
            row.Prefix = '普段は厳格な学者である彼に似合わず、';
            row.Chunk1 = '講義では'; row.Chunk2 = '冗談を'; row.Chunk3 = '交えて'; row.Chunk4 = '優しく語った。';
            row.Suffix = ''; return true;
        }
        if (i === 19) {
            row.Prefix = '私の学校の図書館には、';
            row.Chunk1 = '英語の'; row.Chunk2 = '辞書が'; row.Chunk3 = 'たくさん'; row.Chunk4 = 'あります。';
            row.Suffix = ''; return true;
        }
        if (i === 21) {
            row.Prefix = '恩師の山田先生には、学界の発展に';
            row.Chunk1 = '多大なる'; row.Chunk2 = 'ご尽力を'; row.Chunk3 = 'なさい'; row.Chunk4 = 'ました。';
            row.Suffix = ''; return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_68.csv', (row, i) => {
        if (i === 2) {
            row.Prefix = '言い訳なんか';
            row.Chunk1 = '聞いて'; row.Chunk2 = 'いない。'; row.Chunk3 = '真実が'; row.Chunk4 = '知りたいのだ';
            row.Suffix = '」と刑事は容疑者を鋭く睨みつけた。'; return true;
        }
        if (i === 3) {
            row.Prefix = '彼は日記に';
            row.Chunk1 = '小説の'; row.Chunk2 = 'アイデアを'; row.Chunk3 = '書いたりなんかして、夜遅くまで'; row.Chunk4 = '起きていた。';
            row.Suffix = ''; return true;
        }
        if (i === 4) {
            row.Prefix = 'あの男の甘い言葉なんか、';
            row.Chunk1 = '私は'; row.Chunk2 = '絶対に'; row.Chunk3 = '信じない'; row.Chunk4 = '」と';
            row.Suffix = '彼女は日記に激しい筆跡で書き残した。'; return true;
        }
        if (i === 5) {
            row.Prefix = 'あのような不条理な命令なんか、誰が';
            row.Chunk1 = 'おとなしく'; row.Chunk2 = '従う'; row.Chunk3 = 'もの'; row.Chunk4 = 'か';
            row.Suffix = '」と若き記者は心の中で強く反発した。'; return true;
        }
        if (i === 13) {
            row.Prefix = '絶対に諦めるななんて、';
            row.Chunk1 = '当事者でもない'; row.Chunk2 = '人間に'; row.Chunk3 = '簡単に言って'; row.Chunk4 = 'ほしくない';
            row.Suffix = '」と若者は吐き捨てた。'; return true;
        }
        if (i === 14) {
            row.Prefix = 'この深い海底に未知の巨大生物が';
            row.Chunk1 = '生息して'; row.Chunk2 = 'いるなんて、'; row.Chunk3 = '科学者たちも予想して'; row.Chunk4 = 'いなかった。';
            row.Suffix = ''; return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_67.csv', (row, i) => {
        if (i === 5) {
            row.Prefix = 'この新法案は、環境保護を目的とする';
            row.Chunk1 = '五つの主要な'; row.Chunk2 = '条文'; row.Chunk3 = 'から'; row.Chunk4 = 'なっています。';
            row.Suffix = ''; return true;
        }
        if (i === 9) {
            row.Prefix = '現代社会において、一国の首相とも';
            row.Chunk1 = 'なる'; row.Chunk2 = 'と、'; row.Chunk3 = 'その言動が'; row.Chunk4 = 'メディアに注視される。';
            row.Suffix = ''; return true;
        }
        if (i === 20) {
            row.Prefix = '温かいお茶か';
            row.Chunk1 = 'なんか'; row.Chunk2 = '淹れて、'; row.Chunk3 = '少し'; row.Chunk4 = '休んだらどうかと祖父が言った。';
            row.Suffix = ''; return true;
        }
        return false;
    });

    await fixFile('set_5_jlpt_exam/part_64.csv', (row, i) => {
        if (i === 4) {
            row.Prefix = '普段と違って、彼女の';
            row.Chunk1 = '今日の'; row.Chunk2 = '話し方は'; row.Chunk3 = 'なにか'; row.Chunk4 = 'おかしい。';
            row.Suffix = ''; return true;
        }
        if (i === 8) {
            row.Prefix = 'この古い洋館には、人々を';
            row.Chunk1 = '引きつける'; row.Chunk2 = 'なにかしらの'; row.Chunk3 = '不思議な力がある'; row.Chunk4 = 'ようだ。';
            row.Suffix = ''; return true;
        }
        if (i === 12) {
            row.Prefix = '今回発表された政府の';
            row.Chunk1 = '新たな法案は、'; row.Chunk2 = 'なにがなんでも'; row.Chunk3 = '強引すぎると'; row.Chunk4 = '批判されている。';
            row.Suffix = ''; return true;
        }
        if (i === 14) {
            row.Prefix = '旅先で出会った老人の';
            row.Chunk1 = 'なにげない'; row.Chunk2 = '一言が、'; row.Chunk3 = '私の人生を'; row.Chunk4 = '大きく変えた。';
            row.Suffix = ''; return true;
        }
        if (i === 15) {
            row.Prefix = 'この事件の捜査は、なにしろ手がかりが';
            row.Chunk1 = 'まったく'; row.Chunk2 = 'ないので'; row.Chunk3 = '解決までに'; row.Chunk4 = '長い時間がかかりそうだ。';
            row.Suffix = ''; return true;
        }
        return false;
    });
}

run().catch(console.error);
