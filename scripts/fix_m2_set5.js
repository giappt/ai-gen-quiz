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
    
    // Custom fix for part_91
    if (row['Original Example'] && row['Original Example'].includes('prompt has: ①春の凰に誘われるままに、公園を散歩した。) -> Yes')) {
        row['Original Example'] = '春の風に誘われるままに、公園を散歩した。';
        row['Prefix'] = '春の風に';
        row['Chunk1'] = '誘われる';
        row['Chunk2'] = 'ままに、';
        row['Chunk3'] = '公園を';
        row['Chunk4'] = '散歩した。';
        row['Suffix'] = '';
        row['Explanation'] = 'Phân tích ngữ pháp: Động từ bị động 「誘われる」 kết hợp với 「ままに」 thể hiện ý nghĩa để mặc cho gió mùa xuân cuốn đi. Thứ tự logic 1-2-3-4. Đây là một cấu trúc ngữ pháp quan trọng cần ghi nhớ để nắm vững ý nghĩa câu.';
        isFixed = true;
    }
    
    // Fix typos in chunks
    const cols = ['Prefix', 'Chunk1', 'Chunk2', 'Chunk3', 'Chunk4', 'Suffix', 'Original Example'];
    for (const col of cols) {
        if (row[col]) {
            let originalText = row[col];
            let newText = originalText
                .replace(/個 nhân/g, '個人')
                .replace(/의/g, 'の')
                .replace(/ là m/g, ' làm')
                .replace(/ là \./g, ' là.')
                .replace(/はm /g, 'làm ')
                .replace(/は m /g, 'làm ');
            if (newText !== originalText) {
                row[col] = newText;
                isFixed = true;
            }
        }
    }
    
    // Multi-line in Suffix fix
    let suffix = row['Suffix'] || '';
    if (suffix.includes('\n') || suffix.includes('\r')) {
        suffix = suffix.split(/\r?\n/)[0].replace(/"$/, '').replace(/」$/, '」');
        row['Suffix'] = suffix;
        isFixed = true;
        if (row['Original Example'] && (row['Original Example'].includes('\n') || row['Original Example'].includes('\r'))) {
            row['Original Example'] = row['Original Example'].split(/\r?\n/)[0].replace(/"$/, '');
        }
    }
    
    // Reconstruct
    const original = (row['Original Example'] || '').trim();
    const prefix = (row['Prefix'] || '');
    const c1 = (row['Chunk1'] || '');
    const c2 = (row['Chunk2'] || '');
    const c3 = (row['Chunk3'] || '');
    const c4 = (row['Chunk4'] || '');
    const suffix2 = (row['Suffix'] || '');
    
    const reconstructed = prefix + c1 + c2 + c3 + c4 + suffix2;
    if (original !== reconstructed && c1) {
        if (original.includes('」') && !reconstructed.includes('」')) {
            // Keep original? No, original might have weird formatting.
        }
        
        // Let's strip Vietnamese from Suffix if it crept in, and put in explanation
        if (vietnameseRegex.test(suffix2)) {
            let splitIndex = -1;
            for (let i = 0; i < suffix2.length; i++) {
                if (vietnameseRegex.test(suffix2[i])) {
                    splitIndex = i;
                    break;
                }
            }
            if (splitIndex !== -1) {
                let actualSplit = splitIndex;
                while (actualSplit > 0 && suffix2[actualSplit - 1] !== '。' && suffix2[actualSplit - 1] !== '！' && suffix2[actualSplit - 1] !== '？') {
                    actualSplit--;
                    if (suffix2[actualSplit] === '"' || suffix2[actualSplit] === '「' || suffix2[actualSplit] === 'Cấu' || suffix2[actualSplit] === 'Ngữ') break;
                }
                if (actualSplit > 0 || !row['Explanation']) {
                    const realSuffix = suffix2.substring(0, actualSplit).trim();
                    const explanationPart = suffix2.substring(actualSplit).trim();
                    if (!row['Explanation'] || row['Explanation'].trim() === '') {
                        row['Explanation'] = explanationPart;
                    }
                    row['Suffix'] = realSuffix;
                    isFixed = true;
                }
            }
        }
        
        const r2 = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
        // If Reconstructed contains no Vietnamese, trust it over original
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
