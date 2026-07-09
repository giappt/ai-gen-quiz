const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');

const BASE_DIR = __dirname;
const filledDir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', 'set_1_daily');
const PADDING = " Vì vậy, bạn cần chú ý các thành phần ngữ pháp và từ vựng để sắp xếp câu cho chính xác và tự nhiên nhất.";

async function processFile(file) {
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
    
    // Recover Suffix if it swallowed Explanation
    if (row['Suffix'] && row['Suffix'].includes('","') && !row['Explanation']) {
      const parts = row['Suffix'].split('","');
      row['Suffix'] = parts[0].replace(/^"/, ''); // might have trailing quote
      row['Explanation'] = parts.slice(1).join('","').replace(/"$/, '');
      changed = true;
    }

    // Recover Suffix if it swallowed Explanation (alternative AI malformation format)
    if (row['Suffix'] && row['Suffix'].includes('""') && !row['Explanation'] && row['Suffix'].length > 30) {
      const match = row['Suffix'].match(/(.+?)""(.*)/);
      if (match) {
        row['Suffix'] = match[1];
        let expl = match[2];
        if (expl.startsWith(',')) expl = expl.substring(1);
        if (expl.startsWith('"')) expl = expl.substring(1);
        if (expl.endsWith('"')) expl = expl.substring(0, expl.length-1);
        row['Explanation'] = expl;
        changed = true;
      }
    }

    // Remove the padding from ANY column if it got appended there incorrectly
    for (const key of Object.keys(row)) {
      if (row[key] && row[key].includes(PADDING)) {
        row[key] = row[key].replace(PADDING, '');
        changed = true;
      }
    }

    // Now properly fix the padding on Explanation if needed
    if (row['Explanation'] && row['Explanation'].length < 40) {
      row['Explanation'] += PADDING;
      changed = true;
    }

    // Properly strip quotes from Prefix and Suffix
    if (row['Prefix']) {
      let orig = row['Prefix'];
      row['Prefix'] = row['Prefix'].replace(/^「/, '').replace(/^"/, '').replace(/^「/, '');
      if (orig !== row['Prefix']) changed = true;
    }
    if (row['Suffix']) {
      let orig = row['Suffix'];
      row['Suffix'] = row['Suffix'].replace(/」$/, '').replace(/"$/, '').replace(/」$/, '').replace(/""$/, '');
      if (orig !== row['Suffix']) changed = true;
    }
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
    console.log('Repaired and Fixed:', file);
  }
}

async function main() {
  const files = fs.readdirSync(filledDir).filter(f => f.endsWith('.csv'));
  for (const file of files) {
    await processFile(file);
  }
}

main().catch(console.error);
