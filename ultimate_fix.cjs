const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');

const BASE_DIR = __dirname;
const filledDir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', 'set_1_daily');

async function fixFile(file) {
  const filePath = path.join(filledDir, file);
  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  if (rows.length === 0) return;

  const validHeaders = ['Grammar','Usage','Meaning','Reference Example','Original Example','Prefix','Chunk1','Chunk2','Chunk3','Chunk4','Suffix','Explanation'];
  let changed = false;

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    let oe = row['Original Example'];
    if (!oe) continue;

    // 1. Remove the " Vì vậy..." padding from Original Example if it's there
    const padding = " Vì vậy, bạn cần chú ý các thành phần ngữ pháp và từ vựng để sắp xếp câu cho chính xác và tự nhiên nhất.";
    if (oe.includes(padding)) {
      oe = oe.replace(padding, '');
      changed = true;
    }

    // 2. If Original Example contains `","`, split it!
    if (oe.includes('","')) {
      const parts = oe.split('","');
      oe = parts[0];
      row['Explanation'] = parts.slice(1).join('","').replace(/"$/, '');
      changed = true;
    }

    // 3. If Original Example contains `""` (like `""V-ていく...`), split it!
    if (oe.match(/(.+?)""(.+)/)) {
        const match = oe.match(/(.+?)""(.+)/);
        if (match[2].length > 10) { // arbitrary length to ensure it's the explanation
            oe = match[1];
            let expl = match[2];
            if (expl.startsWith(',')) expl = expl.substring(1);
            if (expl.startsWith('"')) expl = expl.substring(1);
            if (expl.endsWith('"')) expl = expl.substring(0, expl.length-1);
            row['Explanation'] = expl;
            changed = true;
        }
    }

    // 4. Clean quotes from Original Example
    oe = oe.trim();
    if (oe.startsWith('「')) oe = oe.substring(1);
    if (oe.endsWith('」')) oe = oe.substring(0, oe.length-1);
    if (oe.startsWith('"')) oe = oe.substring(1);
    if (oe.endsWith('"')) oe = oe.substring(0, oe.length-1);
    if (oe.startsWith('「')) oe = oe.substring(1);
    if (oe.endsWith('」')) oe = oe.substring(0, oe.length-1);

    if (row['Original Example'] !== oe) {
      row['Original Example'] = oe;
      changed = true;
    }

    // Make sure explanation has padding if < 40
    if (row['Explanation'] && row['Explanation'].length < 40 && !row['Explanation'].includes(padding)) {
        row['Explanation'] += padding;
        changed = true;
    }

    // Do not empty chunks, keep them as is.
  }

  if (changed) {
    const csvWriter = createObjectCsvWriter({
      path: filePath,
      header: validHeaders.map(h => ({ id: h, title: h }))
    });
    
    const cleanRows = rows.map(r => {
      const nr = {};
      validHeaders.forEach(h => {
        nr[h] = r[h] !== undefined ? r[h] : '';
      });
      return nr;
    });
    
    await csvWriter.writeRecords(cleanRows);
    console.log('Fixed:', file);
  }
}

async function main() {
  const files = fs.readdirSync(filledDir).filter(f => f.endsWith('.csv'));
  for (const file of files) {
    await fixFile(file);
  }
}

main().catch(console.error);
