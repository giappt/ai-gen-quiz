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
  ['息子がゲームに,夢중에,なっているので、', '息子がゲームに,夢中に,なっているので、']
]);

fix('mondai2_ordering/csv_filled/set_1_daily/part_24.csv', [
  [',玄関のドアを開けた,開けた,"瞬間に、",美味しそうな,カレーの匂いがした。', ',玄関のドアを,開けた,"瞬間に、",美味しそうな,カレーの匂いがした。']
]);
