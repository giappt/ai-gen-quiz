const fs = require('fs');

let c;
const p11 = 'mondai2_ordering/csv_filled/set_1_daily/part_11.csv';
c = fs.readFileSync(p11, 'utf8');
c = c.replace(/おもいます/g, '思います');
fs.writeFileSync(p11, c);

const p20 = 'mondai2_ordering/csv_filled/set_1_daily/part_20.csv';
c = fs.readFileSync(p20, 'utf8');
c = c.replace('Sai. Ý nghĩa không phù hợp.', 'Sai. Ý nghĩa không phù hợp với cấu trúc ngữ pháp.');
c = c.replace('Sai. Không diễn tả được sự việc trái ngược.', 'Sai. Không diễn tả được sự việc trái ngược như mong đợi.');
c = c.replace('Nhấn mạnh một điều hiển nhiên.','Nhấn mạnh một điều hiển nhiên, trái với mong đợi thông thường.');
fs.writeFileSync(p20, c);

const p7 = 'mondai2_ordering/csv_filled/set_1_daily/part_7.csv';
c = fs.readFileSync(p7, 'utf8');
c = c.replace(/"親友からこんなに素敵な誕生日プレゼントをもらえるなんて、"/g, '親友からこんなに素敵な誕生日プレゼントをもらえるなんて、');
c = c.replace(/"評判だが、"/g, '評判だが、');
c = c.replace(/"一方、"/g, '一方、');
fs.writeFileSync(p7, c);

console.log('Fixed csv_filled');
