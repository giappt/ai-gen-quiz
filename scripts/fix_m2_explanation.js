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

  let fixedCount = 0;
  let headers = Object.keys(rows[0]);

  rows.forEach(row => {
    if (!row['Original Example']) return;

    let isModified = false;
    let expl = (row['Explanation'] || '').trim();
    let orig = (row['Original Example'] || '').trim();
    let suffix = (row['Suffix'] || '').trim();
    let c1 = (row['Chunk1'] || '');
    let c2 = (row['Chunk2'] || '');
    let c3 = (row['Chunk3'] || '');
    let c4 = (row['Chunk4'] || '');
    let prefix = (row['Prefix'] || '');

    // Extract explanation hidden in Original Example or Suffix or Chunks
    const fieldsToCheck = ['Original Example', 'Suffix', 'Chunk4', 'Chunk3', 'Chunk2', 'Chunk1', 'Prefix'];
    let extractedExpl = '';

    for (const field of fieldsToCheck) {
      let val = row[field] || '';
      // If the field has Vietnamese text and it's long enough, it probably contains the explanation.
      if (val.length > 20 && vietnameseRegex.test(val)) {
        // Find where the explanation starts. Usually after '。' or just the first Latin uppercase letter.
        // Look for common keywords.
        const match = val.match(/(Cấu trúc|Mẫu câu|Phó từ|Danh từ|Từ nối|Liên từ|Thể|Động từ|Chunk|Ý nghĩa|Sử dụng|Câu này|Trạng từ|Ở đây|Phần|Trong).*$/);
        if (match && vietnameseRegex.test(match[0])) {
           extractedExpl = match[0];
           // Remove extracted explanation from the field
           row[field] = val.replace(extractedExpl, '').trim();
           // Clean up trailing commas or quotes
           row[field] = row[field].replace(/[,"\s]+$/, '');
           
           if (!expl || expl.length < 20) {
             expl = extractedExpl.replace(/^["\s,]+/, '').replace(/["\s,]+$/, '');
           }
           isModified = true;
        } else {
           // Fallback: split by '。'
           const parts = val.split('。');
           if (parts.length > 1) {
              const potentialExpl = parts.slice(1).join('。').trim();
              if (potentialExpl.length > 20 && vietnameseRegex.test(potentialExpl)) {
                 extractedExpl = potentialExpl;
                 row[field] = parts[0] + '。';
                 if (!expl || expl.length < 20) {
                    expl = extractedExpl.replace(/^["\s,]+/, '').replace(/["\s,]+$/, '');
                 }
                 isModified = true;
              }
           }
        }
      }
    }

    if (isModified) {
      row['Explanation'] = expl;
      
      // Re-construct Original Example if it was modified
      orig = row['Prefix'] + row['Chunk1'] + row['Chunk2'] + row['Chunk3'] + row['Chunk4'] + row['Suffix'];
      if (!orig.endsWith('。') && row['Chunk1']) {
        orig += '。';
        row['Suffix'] += '。';
      }
      row['Original Example'] = orig;
      fixedCount++;
    }
  });

  if (fixedCount > 0) {
    const csvWriter = createObjectCsvWriter({
      path: filePath,
      header: headers.map(h => ({ id: h, title: h }))
    });
    rows.forEach(r => {
      headers.forEach(h => {
        if (r[h] === undefined) r[h] = '';
      });
    });
    await csvWriter.writeRecords(rows);
  }
  
  return fixedCount;
}

async function run() {
  let totalFixed = 0;
  
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_cleaned');
  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        const fixed = await processFile(path.join(m2Dir, set, file));
        totalFixed += fixed;
      }
    }
  }

  console.log(`Total rows explanation aggressively fixed: ${totalFixed}`);
}

run().catch(console.error);
