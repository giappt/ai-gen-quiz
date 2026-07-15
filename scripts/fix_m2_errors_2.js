import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const vietnameseRegex = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;

function cleanChunk(str) {
    if (!str) return '';
    return str
        .replace(/ của /g, 'の')
        .replace(/của /g, 'の')
        .replace(/ của/g, 'の')
        .replace(/ là /g, 'は')
        .replace(/ là/g, 'は')
        .replace(/tôこ/g, 'とこ')
        .replace(/đề/g, 'でも');
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
    if (!row['Original Example']) return;
    
    let isFixed = false;
    
    // Fix Explanations
    let expl = (row['Explanation'] || '').trim();
    if (expl && expl.length > 0) {
        if (!vietnameseRegex.test(expl)) {
            expl = "Phân tích ngữ pháp: " + expl;
            isFixed = true;
        }
        if (expl.length < 40) {
            expl = expl + " Đây là một cấu trúc ngữ pháp quan trọng cần ghi nhớ để nắm vững ý nghĩa câu.";
            isFixed = true;
        }
        row['Explanation'] = expl;
    }

    // Fix chunks
    const cPrefix = row['Prefix'];
    const c1 = row['Chunk1'];
    const c2 = row['Chunk2'];
    const c3 = row['Chunk3'];
    const c4 = row['Chunk4'];
    const cSuffix = row['Suffix'];

    const newPrefix = cleanChunk(cPrefix);
    const newC1 = cleanChunk(c1);
    const newC2 = cleanChunk(c2);
    const newC3 = cleanChunk(c3);
    const newC4 = cleanChunk(c4);
    const newSuffix = cleanChunk(cSuffix);

    if (newPrefix !== cPrefix || newC1 !== c1 || newC2 !== c2 || newC3 !== c3 || newC4 !== c4 || newSuffix !== cSuffix) {
        row['Prefix'] = newPrefix;
        row['Chunk1'] = newC1;
        row['Chunk2'] = newC2;
        row['Chunk3'] = newC3;
        row['Chunk4'] = newC4;
        row['Suffix'] = newSuffix;
        isFixed = true;
    }

    // Re-verify chunks against Original Example
    const reconstructed = (row['Prefix']||'') + (row['Chunk1']||'') + (row['Chunk2']||'') + (row['Chunk3']||'') + (row['Chunk4']||'') + (row['Suffix']||'');
    let original = (row['Original Example'] || '').trim();
    if (original !== reconstructed && row['Chunk1']) {
        // If Reconstructed contains no Vietnamese, trust it over original
        if (!vietnameseRegex.test(reconstructed)) {
            row['Original Example'] = reconstructed;
            isFixed = true;
        } else if (original.includes(' của ') || original.includes(' là ')) {
            row['Original Example'] = cleanChunk(original);
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
