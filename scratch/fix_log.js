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

function updateFile(subDir, file, callback) {
    const fp = path.join(repoDir, subDir, 'csv_filled/set_1_daily', file);
    if (!fs.existsSync(fp)) {
        console.log('File not found:', fp);
        return;
    }
    const results = [];
    let headers = [];
    fs.createReadStream(fp)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('headers', h => { headers = h; })
      .on('data', data => results.push(data))
      .on('end', () => {
          callback(results);
          let content = '\uFEFF' + headers.map(escapeCSV).join(',') + '\n';
          for (const row of results) {
              content += headers.map(h => escapeCSV(row[h])).join(',') + '\n';
          }
          fs.writeFileSync(fp, content, 'utf8');
          console.log('Fixed', file);
      });
}

// 1. part_34.csv
updateFile('mondai2_ordering', 'part_34.csv', results => {
    for (let r of results) {
        if (r['Original Example'] === 'không mong muốn.') {
            r['Original Example'] = '彼が失敗したのは、ひとつには準備不足だったためである。';
            r['Prefix'] = '彼が失敗したのは、';
            r['Chunk1'] = 'ひとつには';
            r['Chunk2'] = '準備不足';
            r['Chunk3'] = 'だった';
            r['Chunk4'] = 'ため';
            r['Suffix'] = 'である。';
            r['Explanation'] = 'Lý do thất bại là do thiếu chuẩn bị (ためである).';
        }
    }
});

// 2. part_41.csv
updateFile('mondai2_ordering', 'part_41.csv', results => {
    for (let r of results) {
        if (r['Original Example'] === 'そこの赤いバッグを見せてください。') {
            r['Original Example'] = 'そこの赤いバッグを私に見せてください。';
        }
        if (r['Original Example'] === 'そこの塩を取ってくださる？') {
            r['Original Example'] = 'そこの塩を私にちょっと取ってくださる？';
        }
    }
});

// 3. part_46.csv
updateFile('mondai2_ordering', 'part_46.csv', results => {
    for (let r of results) {
        if (r['Original Example'] && r['Original Example'].includes('crumbs')) {
            if (r['Original Example'].includes('言葉だけでなく、実際の行動')) {
                r['Original Example'] = '言葉だけでなく、実際の行動でもって気持ちを伝えよう。';
                r['Chunk3'] = 'でもって';
            } else if (r['Original Example'].includes('あのカレー屋は安くて美味しい。')) {
                r['Original Example'] = 'あのカレー屋は安くて美味しい。でもって駅から歩いてすぐの場所にあるんだ。';
                r['Chunk1'] = 'でもって';
            } else if (r['Original Example'].includes('妹は私の冗談に対して、怒る')) {
                r['Original Example'] = '妹は私の冗談に対して、怒るでもなくフッと笑った。';
                r['Chunk2'] = 'でも';
            }
        }
    }
});
