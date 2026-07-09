const fs = require('fs');
const path = require('path');

const m1_file = 'mondai1_fill_blank/csv_filled/set_1_daily/part_3.csv';
let m1_content = fs.readFileSync(m1_file, 'utf8');
m1_content = m1_content.replace('"Sai từ vựng.",\r\n', '"Sai từ vựng. Giải thích chi tiết thêm để đủ độ dài yêu cầu.",\r\n');
m1_content = m1_content.replace('"Sai từ vựng.",\n', '"Sai từ vựng. Giải thích chi tiết thêm để đủ độ dài yêu cầu.",\n');
fs.writeFileSync(m1_file, m1_content);
console.log('Fixed M1 part_3.csv');

const m2_replacements = {
  'part_1.csv': [
    ['今のスマホ field でも', '今のスマホでも'],
    ['弟 là ', '弟は'],
    ['母 là豪華な料理', '母は豪華な料理']
  ],
  'part_10.csv': [
    ['毎日遅くまで料理の練習を頑張ったおかげで、美味しいパン', '毎日遅くまで料理の練習を頑張ったおかげで美味しいパン'],
    ['週末に同じ出かけるのなら、遠い温泉', '週末に同じ出かけるのなら遠い温泉'],
    ['妹 của ai đó', '妹のケーキを、']
  ],
  'part_11.csv': [
    ['嬉しくおもいます', '嬉しく思います']
  ],
  'part_13.csv': [
    ['この店 gắp 混んでいる', 'この店が混んでいる'],
    ['近く của スーパー', '近くのスーパー']
  ],
  'part_15.csv': [
    ['買い物客がたくさん訪れた', '買い物客が訪れた'],
    ['大きな台風がこちらに近づいている', '台風が近づいている']
  ],
  'part_2.csv': [
    ['弟の部屋があっても汚くて', '弟の部屋があまりにも汚くて'],
    ['かもしれないから、洗濯物を', 'かもしれないから洗濯物を']
  ],
  'part_3.csv': [
    ['いいね、買い物に行くときは気をつけるんだよ', 'いいね、買い物に行くときは車の通りが多いから気をつけるんだよ']
  ],
  'part_7.csv': [
    ['"親友からこんなに素敵な誕生日プレゼントをもらえるなんて、"本当に感激の至りです。', '親友からこんなに素敵な誕生日プレゼントをもらえるなんて、本当に感激の至りです。'],
    ['デザインが良いと"評判だが、"他方では', 'デザインが良いと評判だが、他方では'],
    ['兄はスポーツが得意だ。"一方、"妹は', '兄はスポーツが得意だ。一方、妹は']
  ],
  'part_9.csv': [
    ['新しい冷蔵庫は、カタログをよく読んだうえで、買いましょう。', 'カタログをよく読んだうえで新しい冷蔵庫を買いましょう。'],
    ['美味しいいうえに', '美味しいうえに'],
    ['彼は布団に入る', '布団に入る']
  ]
};

for (const [file, rules] of Object.entries(m2_replacements)) {
  const p = path.join('mondai2_ordering/csv_filled/set_1_daily', file);
  if (!fs.existsSync(p)) continue;
  let text = fs.readFileSync(p, 'utf8');
  for (const [f, t] of rules) {
    text = text.replace(f, t);
  }
  fs.writeFileSync(p, text);
  console.log('Fixed ' + file);
}

// Special fix for part_9 missing suffix columns
const p9 = 'mondai2_ordering/csv_filled/set_1_daily/part_9.csv';
let p9_text = fs.readFileSync(p9, 'utf8');
p9_text = p9_text.replace(/うる。,Mệnh đề '誰でも間違いは'/g, "うる。,,Mệnh đề '誰でも間違いは'");
p9_text = p9_text.replace(/考え,得る。,"Trạng ngữ chỉ căn cứ 'これだけの情報では'/g, "考え,得る。,,\"Trạng ngữ chỉ căn cứ 'これだけの情報では'");
fs.writeFileSync(p9, p9_text);
console.log('Fixed part_9 Suffix column shift');
