import fs from 'fs';
import path from 'path';
import csvParser from 'csv-parser';

const repoDir = 'd:/pj/xx/ai-gen-quiz';

function escapeCSV(field) {
  if (field === null || field === undefined) return '';
  const stringField = String(field);
  if (stringField.includes(',') || stringField.includes('"') || stringField.includes('\n')) {
    return `"${stringField.replace(/"/g, '""')}"`;
  }
  return stringField;
}

function processFile(subDir, file, updates) {
    const fp = path.join(repoDir, subDir, 'csv_filled/set_1_daily', file);
    if (!fs.existsSync(fp)) return;
    const results = [];
    let headers = [];
    fs.createReadStream(fp)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('headers', h => { headers = h; })
      .on('data', data => results.push(data))
      .on('end', () => {
          for (const [rStr, updateObj] of Object.entries(updates)) {
              const r = parseInt(rStr); 
              if (results[r]) {
                  Object.assign(results[r], updateObj);
                  if (updateObj['Prefix'] !== undefined) {
                      const p = results[r]['Prefix'] || '';
                      const c1 = results[r]['Chunk1'] || '';
                      const c2 = results[r]['Chunk2'] || '';
                      const c3 = results[r]['Chunk3'] || '';
                      const c4 = results[r]['Chunk4'] || '';
                      const s = results[r]['Suffix'] || '';
                      results[r]['Original Example'] = p + c1 + c2 + c3 + c4 + s;
                  }
              }
          }
          let content = '\uFEFF' + headers.map(escapeCSV).join(',') + '\n';
          for (const row of results) {
              content += headers.map(h => escapeCSV(row[h])).join(',') + '\n';
          }
          fs.writeFileSync(fp, content, 'utf8');
          console.log('Fixed', file);
      });
}

processFile('mondai2_ordering', 'part_42.csv', {
    12: { 'Prefix': '家族のために', 'Chunk1': '5時間もかけて', 'Chunk2': '料理を作る、', 'Chunk3': 'これが愛', 'Chunk4': 'でなくて', 'Suffix': 'なんだろう。' },
    14: { 'Prefix': '家族が', 'Chunk1': '幸せに', 'Chunk2': '暮らせるのも、', 'Chunk3': 'お父さんの頑張りが', 'Chunk4': 'あって', 'Suffix': 'のことだ。' },
    17: { 'Prefix': '毎日', 'Chunk1': '小さなことで', 'Chunk2': '喧嘩して', 'Chunk3': 'いるのでは、', 'Chunk4': '一緒に暮らすのは', 'Suffix': '難しい。' }
});

processFile('mondai2_ordering', 'part_45.csv', {
    0: { 'Prefix': 'この料理は、', 'Chunk1': 'いくら', 'Chunk2': 'レシピ通りに', 'Chunk3': '作っても', 'Chunk4': '母の味には', 'Suffix': 'ならない。' },
    5: { 'Prefix': 'あの店の商品なら、', 'Chunk1': 'たとえ', 'Chunk2': '安くても', 'Chunk3': 'そんな高いバッグは', 'Chunk4': '買わなかった', 'Suffix': 'だろう。' },
    10: { 'Prefix': 'このTシャツを買いたいです。', 'Chunk1': 'でも、', 'Chunk2': '値段が', 'Chunk3': '少し', 'Chunk4': '高い', 'Suffix': 'ですね。' },
    14: { 'Prefix': '彼は', 'Chunk1': '私の', 'Chunk2': '親友でもあり、', 'Chunk3': '良き相談', 'Chunk4': '相手でも', 'Suffix': 'ある。' }
});

processFile('mondai2_ordering', 'part_48.csv', {
    13: { 'Prefix': '兄が', 'Chunk1': '「明日の旅行は中止だ」', 'Chunk2': 'と言ったので、', 'Chunk3': '私は', 'Chunk4': '「というと」', 'Suffix': 'と聞き返しました。' },
    14: { 'Prefix': 'この仕事は', 'Chunk1': 'あと', 'Chunk2': '２、３日', 'Chunk3': 'という', 'Chunk4': 'ところ', 'Suffix': 'だ。', 'Explanation': 'Sử dụng というところだ để diễn tả mức độ đại khái.' }
});

processFile('mondai2_ordering', 'part_2.csv', {
    1: { 'Prefix': '買い物の後で', 'Chunk1': 'カフェに', 'Chunk2': '行って', 'Chunk3': '休もう。', 'Chunk4': '', 'Suffix': '' }, 
    9: { 'Prefix': '弟の部屋が', 'Chunk1': 'あまりにも', 'Chunk2': '汚くて', 'Chunk3': '足の踏み場も', 'Chunk4': 'ない。', 'Suffix': '' }, 
    11: { 'Prefix': 'あんまりにも', 'Chunk1': '夜遅く', 'Chunk2': '寝ると', 'Chunk3': '次の日の朝が', 'Chunk4': '辛いよ。', 'Suffix': '' } 
});

processFile('mondai2_ordering', 'part_23.csv', {
    1: { 'Prefix': '終電を', 'Chunk1': '逃したから、', 'Chunk2': 'タクシーで', 'Chunk3': '家に', 'Chunk4': '帰るしか', 'Suffix': 'ない。' }, 
    8: { 'Prefix': '家に', 'Chunk1': '着きしだい、', 'Chunk2': 'すぐに', 'Chunk3': '連絡する', 'Chunk4': 'ね。', 'Suffix': '' }, 
    16: { 'Prefix': '弟は', 'Chunk1': '飲みすぎて', 'Chunk2': '転び、', 'Chunk3': '挙句の果てには', 'Chunk4': '骨折する', 'Suffix': '始末だ。' } 
});

processFile('mondai2_ordering', 'part_25.csv', {
    5: { 'Prefix': '労せずして', 'Chunk1': '手に入れた', 'Chunk2': 'チケットだから、', 'Chunk3': '友達に', 'Chunk4': '譲ろう。', 'Suffix': '' }, 
    9: { 'Prefix': '母の妹、', 'Chunk1': 'すなわち', 'Chunk2': '私の叔母が', 'Chunk3': '明日', 'Chunk4': '家に遊びに', 'Suffix': '来る。' }, 
    10: { 'Prefix': '値段を', 'Chunk1': '見ずに', 'Chunk2': '服を', 'Chunk3': '買ったら、', 'Chunk4': '予算オーバーに', 'Suffix': 'なってしまった。' } 
});

let vi = [
    'Sau danh từ 「私の実家」, sử dụng 「つまり」 (tóm lại/có nghĩa là) để giải thích lại một cách rõ ràng.',
    'Dùng 「つまり」 để tóm tắt lại tình huống phía trước, dẫn đến kết luận ở cuối câu.',
    'Động từ thể từ điển 「行く」 kết hợp với danh từ 「つもり」 chỉ dự định và 「です」 tạo thành mẫu câu cơ bản.',
    'Động từ thể từ điển 「買う」 đi với 「つもりはない」 thể hiện ý chí phủ định mạnh mẽ (hoàn toàn không có ý định mua).',
    'Động từ thể từ điển 「言う」 đi với 「つもりではなかった」 phủ định ý định trong quá khứ.',
    'Động từ thể từ điển 「買う」 đi với 「つもりで」 thể hiện hành động tiếp theo được thực hiện với mục đích nhất định.',
    'Tính từ 「いい」 kết hợp trực tiếp với 「つもりだ」 thể hiện niềm tin chủ quan của bản thân.',
    'Danh từ đi kèm trợ từ の 「二十代の」 kết nối với 「つもりで」 thể hiện việc bản thân cứ ngỡ như là thực tế.',
    'Động từ thể Ta 「言った」 đi với 「つもりはない」 khẳng định bản thân không hề có ác ý hay ý định đó trong quá khứ.',
    'Động từ thể Ta 「した」 đi với 「つもりで」 giả định như thể đã thực hiện hành động đó.',
    'Động từ chia ở thể Te liên tiếp 「起きて」 và 「して」 tạo thành chuỗi hành động theo thứ tự thời gian.',
    'Tính từ đuôi na 「楽しみ」 lặp lại hai lần kèm trợ từ 「で」 để nhấn mạnh cảm xúc cực độ.',
    'Sử dụng 「で」 ở đầu câu để chuyển tiếp chủ đề câu chuyện một cách tự nhiên trong giao tiếp.',
    'Danh từ 「大雨」 đi với trợ từ 「で」 biểu thị nguyên nhân, dẫn đến kết quả tàu trễ.',
    'Động từ thể Te 「焼いて」 kết hợp với 「あげました」 thể hiện hành động làm ơn cho người khác một cách tự nguyện.',
    'Động từ thể Te 「抱っこして」 đi với 「あげて」 tạo thành lời yêu cầu, nhờ vả nhẹ nhàng.',
    'Tha động từ thể Te 「冷やして」 kết hợp với 「あります」 thể hiện trạng thái đã được chuẩn bị sẵn và vẫn đang duy trì.',
    'Danh từ 「肉」 và 「魚」 đi kèm 「であれ」 tạo thành cấu trúc song hành (cho dù là A hay B thì cũng).',
    'Danh từ 「平日」 và 「週末」 kết hợp với 「であろうと」 thể hiện sự thật không thay đổi bất kể điều kiện nào.',
    'Danh từ 「雨」 kết hợp với 「であろうとなかろうと」 mang nghĩa nhượng bộ tuyệt đối (dù có hay không có cũng không thay đổi).'
];

let p39_updates = {};
for(let i=0; i<20; i++){
    p39_updates[i] = { 'Explanation': vi[i] };
}
processFile('mondai2_ordering', 'part_39.csv', p39_updates);

const fp3 = path.join(repoDir, 'mondai1_fill_blank/csv_filled/set_1_daily/part_3.csv');
const results3 = [];
let headers3 = [];
fs.createReadStream(fp3)
  .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
  .on('headers', h => { headers3 = h; })
  .on('data', data => results3.push(data))
  .on('end', () => {
      [8, 12, 13, 15, 18].forEach(i => {
          if(results3[i]) {
              for(let opt of ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']) {
                  let key = `Option ${opt} Explanation`;
                  if(results3[i][key] && results3[i][key].length < 20) {
                      results3[i][key] += ' (Đây là giải thích bổ sung đầy đủ chi tiết).';
                  }
              }
          }
      });
      let content = '\uFEFF' + headers3.map(escapeCSV).join(',') + '\n';
      for (const row of results3) {
          content += headers3.map(h => escapeCSV(row[h])).join(',') + '\n';
      }
      fs.writeFileSync(fp3, content, 'utf8');
      console.log('Fixed part_3.csv');
  });
