import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

async function processFile(filePath, isM1) {
  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  if (rows.length === 0) return { fixed: 0, total: 0 };

  let fixedCount = 0;
  let headers = Object.keys(rows[0]);

  rows.forEach(row => {
    if (!row['Original Example']) return; // Skip empty
    
    let isFixed = false;
    
    if (isM1) {
      // Heal Correct Answer
      const validAnswers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
      const currentAnswer = (row['Correct Answer'] || '').trim();
      
      if (currentAnswer && !validAnswers.includes(currentAnswer)) {
        for (const opt of validAnswers) {
          if (row[`Option ${opt}`] && row[`Option ${opt}`].trim() === currentAnswer) {
            row['Correct Answer'] = opt;
            isFixed = true;
            break;
          }
        }
      }
    } else {
      // Heal M2 Chunks (remove extra commas or spaces)
      if (row['Chunk1']) {
        const original = (row['Original Example'] || '').trim();
        const prefix = (row['Prefix'] || '');
        const c1 = (row['Chunk1'] || '');
        const c2 = (row['Chunk2'] || '');
        const c3 = (row['Chunk3'] || '');
        const c4 = (row['Chunk4'] || '');
        const suffix = (row['Suffix'] || '');
        
        const currentReconstructed = prefix + c1 + c2 + c3 + c4 + suffix;
        
        if (currentReconstructed !== original) {
          // Attempt 1: Remove all '、' and ' ' from chunks
          const removePunct = (s) => s.replace(/[、\s]/g, '');
          const p_clean = removePunct(prefix);
          const c1_clean = removePunct(c1);
          const c2_clean = removePunct(c2);
          const c3_clean = removePunct(c3);
          const c4_clean = removePunct(c4);
          const s_clean = removePunct(suffix);
          
          if (p_clean + c1_clean + c2_clean + c3_clean + c4_clean + s_clean === original) {
            // It was just a punctuation issue! Update the chunks.
            row['Prefix'] = p_clean;
            row['Chunk1'] = c1_clean;
            row['Chunk2'] = c2_clean;
            row['Chunk3'] = c3_clean;
            row['Chunk4'] = c4_clean;
            row['Suffix'] = s_clean;
            isFixed = true;
          } else {
             // Attempt 2: Vietnamese 'là' typo fix (e.g. 弟 là -> 弟は)
             const fixTypo = (s) => s.replace(/ là /g, 'は').replace(/ là/g, 'は');
             if (fixTypo(currentReconstructed) === original) {
                row['Prefix'] = fixTypo(prefix);
                row['Chunk1'] = fixTypo(c1);
                row['Chunk2'] = fixTypo(c2);
                row['Chunk3'] = fixTypo(c3);
                row['Chunk4'] = fixTypo(c4);
                row['Suffix'] = fixTypo(suffix);
                isFixed = true;
             }
          }
        }
      }
    }
    
    if (isFixed) fixedCount++;
  });

  if (fixedCount > 0) {
    const csvWriter = createObjectCsvWriter({
      path: filePath,
      header: headers.map(h => ({ id: h, title: h }))
    });
    // Ensure we don't write undefined as string
    rows.forEach(r => {
      headers.forEach(h => {
        if (r[h] === undefined) r[h] = '';
      });
    });
    await csvWriter.writeRecords(rows);
  }
  
  return { fixed: fixedCount, total: rows.length };
}

async function run() {
  console.log("Bắt đầu tự động vá lỗi (Fallback Healing)...");
  
  let totalM1Fixed = 0;
  let totalM2Fixed = 0;

  const m1Dir = path.join(BASE_DIR, 'mondai1_fill_blank', 'csv_cleaned');
  if (fs.existsSync(m1Dir)) {
    const sets = fs.readdirSync(m1Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m1Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        const stats = await processFile(path.join(m1Dir, set, file), true);
        totalM1Fixed += stats.fixed;
      }
    }
  }

  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_cleaned');
  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        const stats = await processFile(path.join(m2Dir, set, file), false);
        totalM2Fixed += stats.fixed;
      }
    }
  }

  console.log(`Hoàn tất vá lỗi!`);
  console.log(`Đã vá tự động ${totalM1Fixed} lỗi của Mondai 1.`);
  console.log(`Đã vá tự động ${totalM2Fixed} lỗi của Mondai 2.`);
  console.log("Sếp hãy chạy lại `node review_ai_gen.js` để kiểm tra số lượng lỗi còn tồn đọng nhé!");
}

run().catch(console.error);
