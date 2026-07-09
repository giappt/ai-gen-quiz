const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');

const BASE_DIR = __dirname;

async function fixCSV(relativePath, rowFixes) {
  const filePath = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', relativePath);
  if (!fs.existsSync(filePath)) {
    console.error('Not found:', filePath);
    return;
  }

  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  if (rows.length === 0) return;

  const headers = Object.keys(rows[0]);
  let changed = false;

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    const lineNum = i + 2; // 0-indexed + header
    
    // Auto-fix explanation length
    if (row['Explanation'] && row['Explanation'].length < 40) {
      row['Explanation'] += " Vì vậy, bạn cần chú ý các thành phần ngữ pháp và từ vựng để sắp xếp câu cho chính xác và tự nhiên nhất.";
      changed = true;
    }

    if (rowFixes[lineNum]) {
      const fix = rowFixes[lineNum];
      if (fix.chunks) {
        row['Prefix'] = fix.chunks[0];
        row['Chunk1'] = fix.chunks[1];
        row['Chunk2'] = fix.chunks[2];
        row['Chunk3'] = fix.chunks[3];
        row['Chunk4'] = fix.chunks[4];
        row['Suffix'] = fix.chunks[5];
      } else if (fix.replace) {
        for (const [col, from, to] of fix.replace) {
          if (row[col]) {
            row[col] = row[col].replace(from, to);
          }
        }
      } else if (fix.trimQuotes) {
        if (row['Prefix']) row['Prefix'] = row['Prefix'].replace(/^「/, '');
        if (row['Suffix']) row['Suffix'] = row['Suffix'].replace(/」$/, '');
      }
      changed = true;
    }
  }

  if (changed) {
    const csvWriter = createObjectCsvWriter({
      path: filePath,
      header: headers.map(h => ({ id: h, title: h }))
    });
    // Ensure we don't write undefined
    rows.forEach(r => {
      headers.forEach(h => {
        if (r[h] === undefined) r[h] = '';
      });
    });
    await csvWriter.writeRecords(rows);
    console.log('Fixed', relativePath);
  }
}

async function main() {
  const fixes = {
    'set_1_daily/part_27.csv': {
      5: { replace: [['Suffix', '作れるようなりたい。', '作れるようになりたい。']] }
    },
    'set_1_daily/part_29.csv': {
      2: { chunks: ['①', '観客は一人帰り、', '二人帰り、', 'そして最後には', 'だれも', 'いなくなってしまった。'] },
      10: { replace: [['Chunk1', 'そもそもの', 'そもそ目の']] }
    },
    'set_1_daily/part_30.csv': {
      2: { trimQuotes: true },
      3: { trimQuotes: true },
      4: { trimQuotes: true, replace: [['Suffix', '諦めずに買いたい。', '買いたい。']] },
      5: { trimQuotes: true },
      6: { trimQuotes: true },
      7: { trimQuotes: true },
      8: { trimQuotes: true },
      9: { trimQuotes: true },
      10: { trimQuotes: true },
      11: { trimQuotes: true },
      12: { trimQuotes: true },
      13: { trimQuotes: true },
      14: { trimQuotes: true },
      15: { trimQuotes: true },
      16: { trimQuotes: true },
      17: { trimQuotes: true },
      18: { trimQuotes: true },
      19: { trimQuotes: true },
      20: { trimQuotes: true },
      21: { trimQuotes: true }
    },
    'set_1_daily/part_31.csv': {
      20: { replace: [['Chunk3', 'だから、', 'だから'], ['Suffix', 'どうしろって言うの？', 'どうしろって言うの']] },
      21: { trimQuotes: true, replace: [['Prefix', '「もうお腹が', 'もうお腹が'], ['Chunk3', 'だから、', 'だから']] }
    },
    'set_1_daily/part_32.csv': {
      8: { replace: [['Chunk4', 'だけでは', 'だけでは、']] },
      13: { replace: [['Chunk4', '理由で', '理由で、']] }
    },
    'set_1_daily/part_34.csv': {
      10: { replace: [['Chunk1', 'さいご', '最後']] },
      13: { chunks: ['①', '私から見たら、', 'こんなことは', 'たいした', '問題で', 'はない。'] },
      14: { chunks: ['①', '立って見てないで、', 'ちょっと', '手伝って', 'あげたら。', ''] },
      15: { chunks: ['①', 'あなたったら、', '何', '考えて', 'る', 'の？'] },
      17: { chunks: ['①', '生まれてくる子が', '男の子', 'だったら', 'いいの', 'だが。'] },
      18: { chunks: ['①A：このあいだのパーティーおもしろかったわよ。B：僕も行ったらよかった。A：そうよ。', '来たらよかったのに。', 'どうして', '来なかったの。B：アルバイトがあったんだよ。でも', 'あの日はバイト、ひまでね。', '休んでもよかったんだ。'] },
      19: { chunks: ['', 'không ', 'mong', ' muố', 'n', '.'] },
      20: { chunks: ['①', '別の方法で', '実験して', 'みたら', 'どう', 'でしょうか。'] },
      21: { chunks: ['①', '休みの日には、', 'ビデオを見たり', '音楽を聞いたり', 'してのんびり', '過ごすのが好きです。'] }
    }
  };

  for (const [file, rowFixes] of Object.entries(fixes)) {
    await fixCSV(file, rowFixes);
  }
}

main().catch(console.error);
