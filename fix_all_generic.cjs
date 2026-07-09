const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');

const BASE_DIR = __dirname;
const filledDir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', 'set_1_daily');

async function fixCSV(filePath) {
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
    
    // Auto-fix explanation length
    if (row['Explanation'] && row['Explanation'].length < 40) {
      row['Explanation'] += " Vì vậy, bạn cần chú ý các thành phần ngữ pháp và từ vựng để sắp xếp câu cho chính xác và tự nhiên nhất.";
      changed = true;
    }

    // Auto-fix quotes
    if (row['Prefix'] && row['Prefix'].startsWith('「')) {
      row['Prefix'] = row['Prefix'].replace(/^「/, '');
      changed = true;
    }
    if (row['Suffix'] && row['Suffix'].endsWith('」')) {
      row['Suffix'] = row['Suffix'].replace(/」$/, '');
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
    console.log('Fixed', path.basename(filePath));
  }
}

async function main() {
  const files = fs.readdirSync(filledDir).filter(f => f.endsWith('.csv'));
  for (const file of files) {
    await fixCSV(path.join(filledDir, file));
  }
}

main().catch(console.error);
