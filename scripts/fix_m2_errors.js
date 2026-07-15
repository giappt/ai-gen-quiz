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
  if (!headers.includes('Explanation')) headers.push('Explanation');

  rows.forEach(row => {
    if (!row['Original Example']) return;
    
    let isFixed = false;
    
    // Fix shifted Explanation in Suffix
    const suffix = row['Suffix'] || '';
    if (vietnameseRegex.test(suffix)) {
        const original = (row['Original Example'] || '').trim();
        const prefix = (row['Prefix'] || '');
        const c1 = (row['Chunk1'] || '');
        const c2 = (row['Chunk2'] || '');
        const c3 = (row['Chunk3'] || '');
        const c4 = (row['Chunk4'] || '');
        
        let splitIndex = -1;
        for (let i = 0; i < suffix.length; i++) {
            if (vietnameseRegex.test(suffix[i])) {
                splitIndex = i;
                break;
            }
        }
        
        if (splitIndex !== -1) {
            let actualSplit = splitIndex;
            while (actualSplit > 0 && suffix[actualSplit - 1] !== '。' && suffix[actualSplit - 1] !== '！' && suffix[actualSplit - 1] !== '？') {
                actualSplit--;
                if (suffix[actualSplit] === '"' || suffix[actualSplit] === '「' || suffix[actualSplit] === 'Chủ') break;
            }
            if (actualSplit === 0) {
                if (!row['Explanation']) {
                    row['Explanation'] = suffix;
                    row['Suffix'] = '';
                    isFixed = true;
                }
            } else {
                const realSuffix = suffix.substring(0, actualSplit).trim();
                const explanationPart = suffix.substring(actualSplit).trim();
                if (!row['Explanation'] || row['Explanation'].trim() === '') {
                    row['Explanation'] = explanationPart;
                    row['Suffix'] = realSuffix;
                    isFixed = true;
                }
            }
        }
    }

    // Clean "Chunk X" from Explanation
    if (row['Explanation']) {
        const oldExp = row['Explanation'];
        let newExp = oldExp.replace(/(?:ở\s+)?(?:tại\s+)?\(?(?:Chunk|Chuck|Chunck)\s*\d+(?:\s*\+\s*\d+)*\)?/gi, '');
        newExp = newExp.replace(/\s+/g, ' ').replace(/\(\s*\)/g, '').replace(/\[\s*\]/g, '').trim();
        if (oldExp !== newExp) {
            row['Explanation'] = newExp;
            isFixed = true;
        }
    }

    // Fix Vietnamese typo in Original Example
    let original = (row['Original Example'] || '').trim();
    if (original.includes(' của ')) {
        row['Original Example'] = original.replace(/ của /g, 'の');
        isFixed = true;
    }
    if (original.includes(' là、')) {
        row['Original Example'] = original.replace(/ là、/g, 'は、');
        isFixed = true;
    }
    if (original.includes('tôこ')) {
        row['Original Example'] = original.replace(/tôこ/g, 'とこ');
        isFixed = true;
    }

    // Attempt to match Chunks with Original Example
    original = (row['Original Example'] || '').trim();
    const prefix = (row['Prefix'] || '');
    const c1 = (row['Chunk1'] || '');
    const c2 = (row['Chunk2'] || '');
    const c3 = (row['Chunk3'] || '');
    const c4 = (row['Chunk4'] || '');
    const suffix2 = (row['Suffix'] || '');
    
    const reconstructed = prefix + c1 + c2 + c3 + c4 + suffix2;
    if (original !== reconstructed && c1) {
        if (!vietnameseRegex.test(reconstructed)) {
            row['Original Example'] = reconstructed;
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
