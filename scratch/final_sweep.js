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
    if (!fs.existsSync(fp)) return;
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

updateFile('mondai1_fill_blank', 'part_3.csv', results => {
    for (let i=0; i<10; i++) {
        let row = results[i];
        if (!row) continue;
        let target = row['Correct Answer'];
        if (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'].includes(target)) continue;
        let found = 'A';
        for (let j=0; j<8; j++) {
            let opt = String.fromCharCode(65+j);
            let optVal = row[`Option ${opt}`];
            if (optVal && (optVal === target || optVal.includes(target))) {
                found = opt; break;
            }
        }
        row['Correct Answer'] = found;
    }
});

updateFile('mondai2_ordering', 'part_2.csv', results => {
    let r = results[1];
    if (r) {
        r['Prefix'] = '買い物の後で';
        r['Chunk1'] = 'カフェ';
        r['Chunk2'] = 'に';
        r['Chunk3'] = '行って';
        r['Chunk4'] = '休もう。';
        r['Suffix'] = '';
        r['Original Example'] = r['Prefix']+r['Chunk1']+r['Chunk2']+r['Chunk3']+r['Chunk4']+r['Suffix'];
    }
});

updateFile('mondai2_ordering', 'part_45.csv', results => {
    const addComma = (idx, col) => {
        if(results[idx] && results[idx][col] && !results[idx][col].endsWith('、')) {
            results[idx][col] += '、';
            const p = results[idx]['Prefix']||'';
            const c1 = results[idx]['Chunk1']||'';
            const c2 = results[idx]['Chunk2']||'';
            const c3 = results[idx]['Chunk3']||'';
            const c4 = results[idx]['Chunk4']||'';
            const s = results[idx]['Suffix']||'';
            results[idx]['Original Example'] = p+c1+c2+c3+c4+s;
        }
    };
    addComma(1, 'Prefix'); 
    addComma(2, 'Chunk2'); 
    addComma(3, 'Prefix'); 
    addComma(4, 'Chunk2'); 
    addComma(6, 'Prefix'); 
    addComma(8, 'Chunk1'); 
    addComma(16, 'Prefix'); 
    addComma(18, 'Chunk2'); 
});

updateFile('mondai2_ordering', 'part_48.csv', results => {
    let r = results[13]; 
    if (r) {
        r['Chunk1'] = '「明日の旅行は中止だ」';
        r['Chunk4'] = '「というと」';
        const p = r['Prefix']||''; const c1 = r['Chunk1']||''; const c2 = r['Chunk2']||''; const c3 = r['Chunk3']||''; const c4 = r['Chunk4']||''; const s = r['Suffix']||'';
        r['Original Example'] = p+c1+c2+c3+c4+s;
    }
});
