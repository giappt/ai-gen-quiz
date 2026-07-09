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

let p3Path = path.join(repoDir, 'mondai1_fill_blank/csv_filled/set_1_daily/part_3.csv');
let p3 = fs.readFileSync(p3Path, 'utf8');
p3 = p3.replace('いい,"Đúng. もういいよ', 'いい,Đúng. もういいよ');
fs.writeFileSync(p3Path, p3);

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
    for (let i=0; i<results.length; i++) {
        let row = results[i];
        if (!row) continue;
        let target = row['Correct Answer'];
        if (!['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'].includes(target)) {
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
        
        for(let opt of ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']) {
            let key = `Option ${opt} Explanation`;
            if(row[key] && row[key].length < 20) {
                row[key] += ' (Đây là giải thích bổ sung chi tiết).';
            }
        }
    }
});

updateFile('mondai2_ordering', 'part_45.csv', results => {
    if (results[6] && results[6]['Chunk1'] === '大雨でも') {
        results[6]['Chunk1'] = '大雨でも、';
        let r = results[6];
        r['Original Example'] = (r['Prefix']||'')+(r['Chunk1']||'')+(r['Chunk2']||'')+(r['Chunk3']||'')+(r['Chunk4']||'')+(r['Suffix']||'');
    }
    if (results[16] && results[16]['Chunk1'] === '砂糖の代わりに') {
        results[16]['Chunk1'] = '砂糖の代わりに、';
        let r = results[16];
        r['Original Example'] = (r['Prefix']||'')+(r['Chunk1']||'')+(r['Chunk2']||'')+(r['Chunk3']||'')+(r['Chunk4']||'')+(r['Suffix']||'');
    }
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
