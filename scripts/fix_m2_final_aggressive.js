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
    let isFixed = false;

    let suffix = row['Suffix'] || '';
    if (vietnameseRegex.test(suffix)) {
        let firstVietIndex = -1;
        for(let i=0; i<suffix.length; i++) {
            if (vietnameseRegex.test(suffix[i])) {
                firstVietIndex = i;
                break;
            }
        }
        
        if (firstVietIndex !== -1) {
            let actualSplit = firstVietIndex;
            // backtrack to the end of Japanese sentence
            while (actualSplit > 0 && !['。', '！', '？', '」'].includes(suffix[actualSplit-1])) {
                actualSplit--;
                if (suffix[actualSplit] === '"' || suffix[actualSplit] === '「' || suffix[actualSplit] === 'C' || suffix[actualSplit] === 'N') break;
            }
            
            // if we can't find a clean split, try to just split at firstVietIndex
            if (actualSplit === 0 && !['。', '！', '？', '」'].includes(suffix[0])) {
               // maybe it's all explanation
               actualSplit = 0;
            }

            const realSuffix = suffix.substring(0, actualSplit).trim();
            let explPart = suffix.substring(actualSplit).trim();
            // clean up leading punctuation in explanation
            explPart = explPart.replace(/^["',]+/, '').trim();

            row['Suffix'] = realSuffix.replace(/"$/, '').replace(/,$/, '').trim();
            if (!row['Explanation'] || row['Explanation'].trim() === '') {
                row['Explanation'] = explPart;
            } else if (!row['Explanation'].includes(explPart.substring(0, 20))) {
                // If it doesn't already contain this part, append it
                row['Explanation'] += ' ' + explPart;
            }
            isFixed = true;
        }
    }
    
    // Some lines have Explanation in Original Example as well!
    let original = row['Original Example'] || '';
    if (vietnameseRegex.test(original)) {
        let firstVietIndex = -1;
        for(let i=0; i<original.length; i++) {
            if (vietnameseRegex.test(original[i])) {
                firstVietIndex = i;
                break;
            }
        }
        if (firstVietIndex !== -1) {
            let actualSplit = firstVietIndex;
            while (actualSplit > 0 && !['。', '！', '？', '」'].includes(original[actualSplit-1])) {
                actualSplit--;
            }
            row['Original Example'] = original.substring(0, actualSplit).trim().replace(/"$/, '');
            isFixed = true;
        }
    }
    
    // Now make sure Original Example matches Reconstructed EXACTLY if no Vietnamese is present
    const r2 = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
    if ((row['Original Example'] || '').trim() !== r2) {
        if (!vietnameseRegex.test(r2)) {
            row['Original Example'] = r2;
            isFixed = true;
        }
    }

    if (isFixed) fixedCount++;
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
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled');
  let totalFixed = 0;

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

  console.log(`Fixed ${totalFixed} rows in M2.`);
}

run().catch(console.error);
