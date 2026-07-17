import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import readline from 'readline';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const errorLogPath = path.join(BASE_DIR, 'validation_reports', 'error_log.json');
const allErrors = [];

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

async function updateCsvRow(filePath, originalExample, rowDataToUpdate) {
    const rows = await new Promise((resolve, reject) => {
        const results = [];
        fs.createReadStream(filePath)
            .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
            .on('data', (data) => results.push(data))
            .on('end', () => resolve(results))
            .on('error', reject);
    });

    if (rows.length === 0) return;

    let headers = Object.keys(rows[0]);
    let updated = false;
    for (let r of rows) {
        if (r['Original Example'] === originalExample) {
            Object.assign(r, rowDataToUpdate);
            updated = true;
            break;
        }
    }

    if (updated) {
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
}

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
          if (!isFixed) {
             allErrors.push({
                 file: filePath,
                 type: 'M2_CHUNK_MISMATCH',
                 original: original,
                 reconstructed: currentReconstructed,
                 row: row
             });
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

  const m1Dir = path.join(BASE_DIR, 'mondai1_fill_blank', 'csv_filled');
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

  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled');
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

  // Save error report
  const reportsDir = path.join(BASE_DIR, 'validation_reports');
  if (!fs.existsSync(reportsDir)) {
      fs.mkdirSync(reportsDir, { recursive: true });
  }
  fs.writeFileSync(errorLogPath, JSON.stringify(allErrors, null, 2), 'utf8');

  console.log(`Hoàn tất vá lỗi tự động!`);
  console.log(`Đã vá tự động ${totalM1Fixed} lỗi của Mondai 1.`);
  console.log(`Đã vá tự động ${totalM2Fixed} lỗi của Mondai 2.`);
  
  if (allErrors.length > 0) {
      console.log(`\nĐã tìm thấy ${allErrors.length} lỗi không thể tự vá.`);
      const answer = await askQuestion('Bạn có muốn mở CÔNG CỤ REVIEW TƯƠNG TÁC để sửa thủ công ngay bây giờ không? (y/n) [Mặc định: y]: ');
      
      if (answer.toLowerCase() === 'y' || answer.trim() === '') {
          console.log(`\n=== CÔNG CỤ REVIEW LỖI CHUNK TƯƠNG TÁC ===\n`);
          let interactiveFixedCount = 0;

          for (let i = 0; i < allErrors.length; i++) {
              const err = allErrors[i];
              console.log(`\n[Lỗi ${i + 1}/${allErrors.length}] File: ${path.basename(err.file)}`);
              console.log(`\x1b[31mOriginal     :\x1b[0m ${err.original}`);
              console.log(`\x1b[32mReconstructed:\x1b[0m ${err.reconstructed}`);
              console.log(`Chunks hiện tại:`);
              console.log(`  Prefix: [${err.row.Prefix}]`);
              console.log(`  C1: [${err.row.Chunk1}], C2: [${err.row.Chunk2}], C3: [${err.row.Chunk3}], C4: [${err.row.Chunk4}]`);
              console.log(`  Suffix: [${err.row.Suffix}]`);
              
              console.log(`\nChọn hành động:`);
              console.log(`  1. Ghi đè Original bằng Reconstructed (Original <- Reconstructed)`);
              console.log(`  2. Tự gõ lại câu Original đúng`);
              console.log(`  3. Bỏ qua (Skip)`);
              console.log(`  4. Thoát công cụ (Thoát)`);

              let choice = '';
              while (!['1', '2', '3', '4'].includes(choice)) {
                  choice = await askQuestion("Lựa chọn của bạn (1/2/3/4) [Mặc định: 1]: ");
                  if (choice === '') choice = '1';
              }

              if (choice === '4') {
                  console.log("Đã thoát công cụ.");
                  break;
              }

              if (choice === '3') {
                  console.log("Đã bỏ qua.");
                  continue;
              }

              if (choice === '1') {
                  console.log(`=> Cập nhật Original thành: ${err.reconstructed}`);
                  await updateCsvRow(err.file, err.original, { 'Original Example': err.reconstructed });
                  interactiveFixedCount++;
              } else if (choice === '2') {
                  const customOriginal = await askQuestion("Nhập câu Original đúng: ");
                  if (customOriginal.trim() !== '') {
                      console.log(`=> Cập nhật Original thành: ${customOriginal}`);
                      await updateCsvRow(err.file, err.original, { 'Original Example': customOriginal });
                      interactiveFixedCount++;
                  } else {
                      console.log("Bỏ qua vì đầu vào rỗng.");
                  }
              }
          }
          console.log(`\nHoàn tất! Đã sửa tương tác ${interactiveFixedCount} lỗi.`);
      } else {
          console.log(`Đã ghi lỗi vào: ${errorLogPath}`);
          console.log("Sếp hãy kiểm tra error_log.json để sửa tay hoặc dùng AI sửa các dòng này nhé!");
      }
  }
  rl.close();
}

run().catch(err => {
    console.error(err);
    rl.close();
});
