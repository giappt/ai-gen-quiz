import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const vietnameseRegex = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;

async function processFile(filePath) {
  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  if (rows.length === 0) return 0;
  
  let validRows = [];
  let deletedCount = 0;
  
  rows.forEach(row => {
    if (!row['Original Example']) return; // Skip completely empty

    let isValid = true;
    
    // Check 4 chunks
    const c1 = (row['Chunk1'] || '').trim();
    const c2 = (row['Chunk2'] || '').trim();
    const c3 = (row['Chunk3'] || '').trim();
    const c4 = (row['Chunk4'] || '').trim();
    if (!c1 || !c2 || !c3 || !c4) {
      isValid = false;
    }
    
    // Check explanation
    const expl = row['Explanation'] || '';
    if (expl.length < 40 || !vietnameseRegex.test(expl)) {
      isValid = false;
    }
    
    if (isValid) {
      validRows.push(row);
    } else {
      // Clear the row instead of deleting it to prevent row shifting
      row['Prefix'] = '';
      row['Chunk1'] = '';
      row['Chunk2'] = '';
      row['Chunk3'] = '';
      row['Chunk4'] = '';
      row['Suffix'] = '';
      row['Original Example'] = '';
      row['Explanation'] = '';
      validRows.push(row);
      deletedCount++;
    }
  });

  if (deletedCount > 0) {
    let headers = Object.keys(rows[0] || {});
    if(headers.length === 0) return 0;
    
    const tempPath = filePath + '.tmp';
    const csvWriter = createObjectCsvWriter({
      path: tempPath,
      header: headers.map(h => ({ id: h, title: h }))
    });
    
    await csvWriter.writeRecords(validRows);
    fs.renameSync(tempPath, filePath);
  }
  
  return deletedCount;
}

async function run() {
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled');
  let totalDeleted = 0;
  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        totalDeleted += await processFile(path.join(m2Dir, set, file));
      }
    }
  }
  console.log(`Đã xóa ${totalDeleted} dòng lỗi từ csv_filled.`);
}

run().catch(console.error);
