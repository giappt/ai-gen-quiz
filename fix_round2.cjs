const fs = require('fs');

function fix(file, replaces) {
  let text = fs.readFileSync(file, 'utf8');
  for (let [from, to] of replaces) {
    text = text.replace(from, to);
  }
  fs.writeFileSync(file, text);
  console.log('Fixed ' + file);
}

fix('mondai2_ordering/csv_filled/set_1_daily/part_21.csv', [
  ['息子 gập ゲームに夢중になっているので、', '息子がゲームに夢中になっているので、']
]);

fix('mondai2_ordering/csv_filled/set_1_daily/part_22.csv', [
  ['うち của 猫は', 'うちの猫は']
]);

fix('mondai2_ordering/csv_filled/set_1_daily/part_23.csv', [
  ['主婦 of 愚痴', '主婦の愚痴']
]);

fix('mondai2_ordering/csv_filled/set_1_daily/part_24.csv', [
  ['開けた開けた瞬間に', '開けた瞬間に']
]);

fix('mondai2_ordering/csv_filled/set_1_daily/part_25.csv', [
  ['笑わずにはいられないよ。","友達が送ってきた動画が面白すぎて、","私は","笑わ","ずには","いられない","よ。"', '私は笑わずにはいられないよ。","友達が送ってきた動画が面白すぎて、","私は","笑わ","ずには","いられない","よ。"'],
  ['謝らずにはすまないだろう。","隣の家の窓ガラスを割ってしまったのだから、","直接","謝ら","ずには","すまない","だろう。"', '直接謝らずにはすまないだろう。","隣の家の窓ガラスを割ってしまったのだから、","直接","謝ら","ずには","すまない","だろう。"']
]);
