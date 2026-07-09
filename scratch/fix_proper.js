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

function processFile(file, updates) {
    const fp = path.join(repoDir, 'mondai2_ordering/csv_filled/set_1_daily', file);
    if (!fs.existsSync(fp)) return;
    const results = [];
    let headers = [];
    fs.createReadStream(fp)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('headers', h => { headers = h; })
      .on('data', data => results.push(data))
      .on('end', () => {
          for (const [rStr, updateObj] of Object.entries(updates)) {
              const r = parseInt(rStr) - 1;
              if (results[r]) {
                  Object.assign(results[r], updateObj);
                  const p = results[r]['Prefix'] || '';
                  const c1 = results[r]['Chunk1'] || '';
                  const c2 = results[r]['Chunk2'] || '';
                  const c3 = results[r]['Chunk3'] || '';
                  const c4 = results[r]['Chunk4'] || '';
                  const s = results[r]['Suffix'] || '';
                  results[r]['Original Example'] = p + c1 + c2 + c3 + c4 + s;
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

processFile('part_42.csv', {
    14: { 'Prefix': '家族のために', 'Chunk1': '5時間もかけて', 'Chunk2': '料理を作る、', 'Chunk3': 'これが愛', 'Chunk4': 'でなくて', 'Suffix': 'なんだろう。' },
    16: { 'Prefix': '家族が', 'Chunk1': '幸せに', 'Chunk2': '暮らせるのも、', 'Chunk3': 'お父さんの頑張りが', 'Chunk4': 'あって', 'Suffix': 'のことだ。' },
    19: { 'Prefix': '毎日', 'Chunk1': '小さなことで', 'Chunk2': '喧嘩して', 'Chunk3': 'いるのでは、', 'Chunk4': '一緒に暮らすのは', 'Suffix': '難しい。' }
});

processFile('part_45.csv', {
    2: { 'Prefix': 'この料理は、', 'Chunk1': 'いくら', 'Chunk2': 'レシピ通りに', 'Chunk3': '作っても', 'Chunk4': '母の味には', 'Suffix': 'ならない。' },
    3: { 'Prefix': '私は、', 'Chunk1': 'どんなに', 'Chunk2': '仕事が', 'Chunk3': '忙しくても', 'Chunk4': '毎日家族に', 'Suffix': '電話をかけている。' },
    4: { 'Prefix': '誰が', 'Chunk1': '何と', 'Chunk2': '言っても、', 'Chunk3': '私はこの服を', 'Chunk4': '絶対に', 'Suffix': '買いたい。' },
    5: { 'Prefix': '昨日のことは、', 'Chunk1': 'どう', 'Chunk2': '考えても、', 'Chunk3': '彼女が', 'Chunk4': '怒っている理由が', 'Suffix': 'わからない。' },
    7: { 'Prefix': 'あの店の商品なら、', 'Chunk1': 'たとえ', 'Chunk2': '安くても', 'Chunk3': 'そんな高いバッグは', 'Chunk4': '買わなかった', 'Suffix': 'だろう。' },
    12: { 'Prefix': 'このTシャツを買いたいです。', 'Chunk1': 'でも、', 'Chunk2': '値段が', 'Chunk3': '少し', 'Chunk4': '高い', 'Suffix': 'ですね。' },
    16: { 'Prefix': '彼は', 'Chunk1': '私の', 'Chunk2': '親友でもあり、', 'Chunk3': '良き相談', 'Chunk4': '相手でも', 'Suffix': 'ある。' }
});

processFile('part_48.csv', {
    15: { 'Prefix': '兄が', 'Chunk1': '「明日の旅行は中止だ」', 'Chunk2': 'と言ったので、', 'Chunk3': '私は', 'Chunk4': '「というと」', 'Suffix': 'と聞き返しました。' }
});
