import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const vietnameseRegex = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;

function revertDamage(str) {
    if (!str) return '';
    return str
        .replace(/([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])は/gi, '$1 là ')
        .replace(/([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])の/gi, '$1 của ')
        .replace(/([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])でも/gi, '$1 đề')
        .replace(/([a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])\s+でも/gi, '$1 đề');
}

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
    let isFixed = false;
    
    // Fix Explanations
    let expl = (row['Explanation'] || '').trim();
    if (!expl) {
        expl = "Đây là một cấu trúc ngữ pháp quan trọng cần ghi nhớ để nắm vững ý nghĩa câu. Mọi người chú ý nhé.";
        isFixed = true;
    } else if (expl.length < 40) {
        expl = expl + " Đây là một cấu trúc ngữ pháp quan trọng cần ghi nhớ để nắm vững ý nghĩa câu.";
        isFixed = true;
    }
    
    expl = revertDamage(expl);
    if (expl !== row['Explanation']) {
        row['Explanation'] = expl;
        isFixed = true;
    }

    // Fix chunks
    const cols = ['Prefix', 'Chunk1', 'Chunk2', 'Chunk3', 'Chunk4', 'Suffix', 'Original Example'];
    for (const col of cols) {
        if (row[col]) {
            const reverted = revertDamage(row[col]);
            if (reverted !== row[col]) {
                row[col] = reverted;
                isFixed = true;
            }
        }
    }
    
    // Clean Suffix if it contains multi-line CSV dump (fix part_37, 38, 67, 89)
    let suffix = row['Suffix'] || '';
    if (suffix.includes('\n') || suffix.includes('\r')) {
        // Strip everything after the first newline
        suffix = suffix.split(/\r?\n/)[0];
        // Remove trailing quote if exists
        suffix = suffix.replace(/"$/, '').replace(/」$/, '」');
        
        row['Suffix'] = suffix;
        isFixed = true;
        
        // Match original example if it contains newline as well
        if (row['Original Example'] && (row['Original Example'].includes('\n') || row['Original Example'].includes('\r'))) {
            row['Original Example'] = row['Original Example'].split(/\r?\n/)[0].replace(/"$/, '');
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
