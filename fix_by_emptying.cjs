const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');

const BASE_DIR = __dirname;
const filledDir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', 'set_1_daily');
const reportPath = path.join(BASE_DIR, 'review_report.txt');

async function processFile(file, rowsToEmpty) {
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
    const csvRowNumber = i + 2; // Data rows start at 2
    
    if (rowsToEmpty.includes(csvRowNumber)) {
      const row = rows[i];
      // Empty the chunks to trigger Fallback Healing
      row['Prefix'] = '';
      row['Chunk1'] = '';
      row['Chunk2'] = '';
      row['Chunk3'] = '';
      row['Chunk4'] = '';
      row['Suffix'] = '';
      changed = true;
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
    console.log('Emptied chunks for fallback healing:', file);
  }
}

async function main() {
  const report = fs.readFileSync(reportPath, 'utf8');
  const lines = report.split('\n');
  
  const filesToFix = {};
  
  for (const line of lines) {
    if (line.startsWith('[M2] File: mondai2/set_1_daily/part_')) {
      const match = line.match(/part_(\d+)\.csv \| Dòng (\d+)/);
      if (match) {
        const file = `part_${match[1]}.csv`;
        const row = parseInt(match[2], 10);
        if (!filesToFix[file]) filesToFix[file] = [];
        filesToFix[file].push(row);
      }
    }
  }
  
  for (const [file, rowsToEmpty] of Object.entries(filesToFix)) {
    if (fs.existsSync(path.join(filledDir, file))) {
       await processFile(file, rowsToEmpty);
    }
  }
}

main().catch(console.error);
