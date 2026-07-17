import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

async function fixFile(relativePath, updateFn) {
    const filePath = path.join(BASE_DIR, relativePath);
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
        const headers = Object.keys(rows[0]);
        const csvWriter = createObjectCsvWriter({
            path: filePath,
            header: headers.map(h => ({ id: h, title: h }))
        });
        await csvWriter.writeRecords(rows);
        console.log('Fixed', relativePath);
    }
}

async function run() {
    const fixes = {
        "mondai2_ordering/csv_filled/set_1_daily/part_105.csv": {
            19: { p: "友達のホームパーティーに行ったらテーブルに料理が", c1: "並ぶわ", c2: "並ぶ", c3: "わで", c4: "食べ", s: "きれなかった。" }
        },
        "mondai2_ordering/csv_filled/set_1_daily/part_38.csv": {
            8: { p: "明日のパーティー、本当に来るの？", c1: "行く", c2: "ったら", c3: "行くんだ", c4: "よ。", s: "" }
        },
        "mondai2_ordering/csv_filled/set_1_daily/part_43.csv": {
            2: { p: "弟はクッキーを", c1: "食べては片付け、", c2: "食べて", c3: "は", c4: "片付け、", s: "部屋が汚いままだ。" }
        },
        "mondai2_ordering/csv_filled/set_1_daily/part_48.csv": {
            8: { p: "息子の部屋は、", c1: "散らかっているというか、", c2: "汚い", c3: "という", c4: "か、", s: "本当にひどい状態です。" }
        },
        "mondai2_ordering/csv_filled/set_1_daily/part_98.csv": {
            9: { p: "苦手な料理は、", c1: "食べられない", c2: "ものは", c3: "食べられないと", c4: "言って", s: "断りましょう。" }
        },
        "mondai2_ordering/csv_filled/set_2_business/part_105.csv": {
            19: { p: "新商品の発表会を開催したら、", c1: "注文が来るわ", c2: "来る", c3: "わ", c4: "対応が", s: "追いつかないほどだった。" }
        },
        "mondai2_ordering/csv_filled/set_2_business/part_36.csv": {
            15: { p: "業務においては、", c1: "先輩だろうが、", c2: "後輩", c3: "だろう", c4: "が、", s: "期限を守るべきです。" }
        },
        "mondai2_ordering/csv_filled/set_2_business/part_39.csv": {
            13: { p: "大切なプレゼンの前日は、", c1: "緊張して緊張して", c2: "夜", c3: "も", c4: "眠れません", s: "でした。" }
        },
        "mondai2_ordering/csv_filled/set_2_business/part_59.csv": {
            12: { p: "チームで連日", c1: "調べども調べども、", c2: "システム", c3: "障害の", c4: "原因が", s: "特定できない。" }
        },
        "mondai2_ordering/csv_filled/set_2_business/part_8.csv": {
            8: { p: "午前中に送ったメールの返信が、いまだに届いていないので", c1: "大変", c2: "心配", c3: "です。", c4: "", s: "" }
        },
        "mondai2_ordering/csv_filled/set_2_business/part_95.csv": {
            3: { p: "来週の出張ですが、", c1: "田中さんも", c2: "渡辺", c3: "さん", c4: "も", s: "参加します。" },
            4: { p: "今回のプロジェクトは、", c1: "予算も", c2: "時間", c3: "も", c4: "ないので", s: "大変です。" },
            5: { p: "A：この企画、予算が足りなくて進めるか迷っています。B：", c1: "やるもやらないも", c2: "ない、", c3: "これは", c4: "社長の", s: "指示だよ。" },
            6: { p: "今回のシステム障害は、", c1: "言い訳も", c2: "何も", c3: "ない、", c4: "弊社の", s: "不手際です。" },
            7: { p: "この新商品を市場に", c1: "投入するも", c2: "投入", c3: "しない", c4: "も、", s: "すべて顧客の反応次第だ。" },
            18: { p: "うちの社長は、", c1: "頑固も", c2: "頑固、", c3: "絶対に", c4: "意見を", s: "変えません。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_103.csv": {
            2: { p: "取引先は新しい提案に", c1: "賛成しているような", c2: "反対", c3: "している", c4: "ような", s: "曖昧な態度を示している。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_12.csv": {
            5: { p: "うちの会社は", c1: "社長が", c2: "社長", c3: "だから、", c4: "社員の", s: "モチベーションも上がらないのだ。" },
            6: { p: "今回のプロジェクトは、", c1: "案件が", c2: "案件", c3: "だけに、", c4: "絶対に", s: "失敗は許されない。" },
            7: { p: "時代が", c1: "時代なら、", c2: "我が社も", c3: "大儲けできた", c4: "はずだが、", s: "現在のデフレ下では厳しい。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_39.csv": {
            13: { p: "今週は新商品の", c1: "発売を控えていて、", c2: "忙しくて", c3: "忙しくて", c4: "目が", s: "回りそうです。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_43.csv": {
            2: { p: "企画書を", c1: "修正しては確認し、", c2: "修正して", c3: "は", c4: "確認し、", s: "ようやく提出にこぎつけた。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_59.csv": {
            12: { p: "催促のメールを送ったが、", c1: "待てども待てども", c2: "先方", c3: "からの", c4: "連絡が", s: "ございません。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_73.csv": {
            4: { p: "請求書は", c1: "メールにしても", c2: "郵送", c3: "に", c4: "しても", s: "今月末までにご送付ください。" }
        },
        "mondai2_ordering/csv_filled/set_3_academic/part_78.csv": {
            8: { p: "彼は", c1: "予算が足りないの", c2: "時間が", c3: "無い", c4: "のと", s: "理由をつけて、新しいプロジェクトを引き受けようとしない。" },
            9: { p: "取引先との接待に", c1: "参加するの", c2: "参加", c3: "しない", c4: "のと、", s: "同僚たちが揉めている。" }
        },
        "mondai2_ordering/csv_filled/set_4_literature/part_100.csv": {
            14: { p: "彼女の寂しげな微笑みを見て、", c1: "喜んでいるのやら", c2: "悲しんで", c3: "いる", c4: "のやら", s: "分からなかった。" }
        },
        "mondai2_ordering/csv_filled/set_4_literature/part_105.csv": {
            19: { p: "その話題の小説が発売されると、書店には", c1: "客が押し寄せるわ", c2: "押し寄せる", c3: "わ、", c4: "大混乱と", s: "なった。" }
        },
        "mondai2_ordering/csv_filled/set_4_literature/part_39.csv": {
            13: { p: "犯人の逮捕を聞き、", c1: "被害者の母親は", c2: "悔しくて悔しくて", c3: "ならなかった", c4: "と", s: "涙を拭った。" }
        },
        "mondai2_ordering/csv_filled/set_4_literature/part_95.csv": {
            3: { p: "この本屋には", c1: "新聞も", c2: "雑誌", c3: "も", c4: "あり", s: "ます。" },
            4: { p: "その事件のニュースは、", c1: "嬉しくも", c2: "悲しく", c3: "も", c4: "ない。", s: "" },
            5: { p: "締め切りが迫っているのだから、", c1: "書くも", c2: "書かない", c3: "も", c4: "ない。", s: "" },
            6: { p: "争いの果てに、", c1: "正義も", c2: "何も", c3: "ない", c4: "荒野が", s: "広がっていた。" },
            7: { p: "真実を", c1: "明かすも", c2: "黙っている", c3: "も", c4: "記者の", s: "良心次第だ。" },
            18: { p: "あの政治家は、", c1: "悪党も", c2: "悪党", c3: "最悪の", c4: "男だ。", s: "" }
        },
        "mondai2_ordering/csv_filled/set_5_jlpt_exam/part_50.csv": {
            7: { p: "その豪雪の夜は、", c1: "屋根といわず、", c2: "庭", c3: "と", c4: "いわず、", s: "すべてが白一色に染まった。" }
        },
        "mondai2_ordering/csv_filled/set_5_jlpt_exam/part_78.csv": {
            9: { p: "教授会では、新規の予算を", c1: "申請するの", c2: "申請", c3: "しない", c4: "のと", s: "激しく議論している。" }
        }
    };

    for (const [file, rowFixes] of Object.entries(fixes)) {
        await fixFile(file, (row, i) => {
            if (rowFixes[i]) {
                const fix = rowFixes[i];
                row['Prefix'] = fix.p;
                row['Chunk1'] = fix.c1;
                row['Chunk2'] = fix.c2;
                row['Chunk3'] = fix.c3;
                row['Chunk4'] = fix.c4;
                row['Suffix'] = fix.s;
                
                // Set explanation if any chunks are empty to avoid further script crashes
                if (!fix.c4) {
                    row['Explanation'] = row['Explanation'] + ' [Fixed]';
                }
                return true;
            }
            return false;
        });
    }
}

run().catch(console.error);
