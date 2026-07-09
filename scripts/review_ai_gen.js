import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');
const REPORT_FILE = path.join(__dirname, '..', 'review_report.txt');

// Reset report file
fs.writeFileSync(REPORT_FILE, '--- BÁO CÁO REVIEW CHẤT LƯỢNG DỮ LIỆU AI-GEN ---\n\n');
let totalErrors = 0;
let totalChecked = 0;

// Regex kiểm tra tiếng Việt (có dấu)
const vietnameseRegex = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;


function logError(msg) {
  fs.appendFileSync(REPORT_FILE, msg + '\n');
  console.log(msg);
  totalErrors++;
}

async function validateM1(filePath, relativePath) {
  const rows = await readCSV(filePath);
  if (rows.length === 0) return;

  rows.forEach((row, index) => {
    const lineNum = index + 2; // +1 for header, +1 for 0-index
    // Skip empty rows (unfilled)
    if (!row['Original Example'] || !row['Blanked Example']) return;
    
    totalChecked++;
    let hasError = false;
    let errorMsgs = [];

    // 1. Kiểm tra dấu đục lỗ
    if (!row['Blanked Example'].includes('___')) {
      hasError = true;
      errorMsgs.push('Thiếu ký hiệu đục lỗ "___" trong Blanked Example.');
    }

    // 2. Kiểm tra Correct Answer hợp lệ
    const validAnswers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    if (!validAnswers.includes(row['Correct Answer'])) {
      hasError = true;
      errorMsgs.push(`Correct Answer sai định dạng (Hiện tại: ${row['Correct Answer']}). Phải là A, B, C... H.`);
    }

    // 3. Kiểm tra đáp án trùng lặp & độ dài giải thích
    const options = [];
    for (const opt of validAnswers) {
      const optText = row[`Option ${opt}`];
      const optExpl = row[`Explanation ${opt}`];
      
      if (optText) {
        if (options.includes(optText)) {
          hasError = true;
          errorMsgs.push(`Đáp án trùng lặp phát hiện: "${optText}" ở Option ${opt}.`);
        }
        options.push(optText);
        
        if (!optExpl || optExpl.length < 20) {
          hasError = true;
          errorMsgs.push(`Giải thích cho Option ${opt} quá ngắn hoặc trống (< 20 ký tự).`);
        } else if (!vietnameseRegex.test(optExpl)) {
          hasError = true;
          errorMsgs.push(`Giải thích cho Option ${opt} dường như không phải tiếng Việt (thiếu dấu).`);
        }
      }
    }

    if (hasError) {
      logError(`[M1] File: ${relativePath} | Dòng ${lineNum}`);
      errorMsgs.forEach(m => logError(`     -> ${m}`));
    }
  });
}

async function validateM2(filePath, relativePath) {
  const rows = await readCSV(filePath);
  if (rows.length === 0) return;

  rows.forEach((row, index) => {
    const lineNum = index + 2;
    if (!row['Original Example']) return;

    totalChecked++;
    let hasError = false;
    let errorMsgs = [];

    // 1. Kiểm tra độ dài & ngôn ngữ Explanation
    const expl = row['Explanation'] || '';
    if (expl.length < 40) {
      hasError = true;
      errorMsgs.push('Giải thích quá ngắn (< 40 ký tự). Cần mô tả kỹ hơn lý do sắp xếp.');
    } else if (!vietnameseRegex.test(expl)) {
      hasError = true;
      errorMsgs.push('Giải thích dường như không phải tiếng Việt (thiếu dấu).');
    }

    // 2. Kiểm tra ghép nối Chunk có khớp 100% với Original Example không
    const original = (row['Original Example'] || '').trim();
    // Bỏ qua các dòng trống chưa điền
    if (!row['Chunk1']) return;

    const prefix = (row['Prefix'] || '').trim();
    const c1 = (row['Chunk1'] || '').trim();
    const c2 = (row['Chunk2'] || '').trim();
    const c3 = (row['Chunk3'] || '').trim();
    const c4 = (row['Chunk4'] || '').trim();
    const suffix = (row['Suffix'] || '').trim();

    if (!c1 || !c2 || !c3 || !c4) {
      hasError = true;
      errorMsgs.push('Thiếu một trong 4 chunks bắt buộc.');
    } else {
      const reconstructed = prefix + c1 + c2 + c3 + c4 + suffix;
      // Normalize to avoid whitespace/width issues (optional, but good for robust testing)
      const normalize = (str) => str.replace(/\s+/g, '').replace(/。/g, '');
      
      if (normalize(reconstructed) !== normalize(original)) {
        hasError = true;
        errorMsgs.push(`Ghép câu thất bại! Chunks bị biến tấu so với câu gốc.`);
        errorMsgs.push(`     Gốc : ${original}`);
        errorMsgs.push(`     Ghép: ${reconstructed}`);
      }
    }

    if (hasError) {
      logError(`[M2] File: ${relativePath} | Dòng ${lineNum}`);
      errorMsgs.forEach(m => logError(`     -> ${m}`));
    }
  });
}

function readCSV(filePath) {
  return new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });
}

async function run() {
  console.log("Bắt đầu quét Validate dữ liệu AI-Gen...");
  
  const m1Dir = path.join(BASE_DIR, 'mondai1_fill_blank', 'csv_cleaned');
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_cleaned');

  // Quét M1
  if (fs.existsSync(m1Dir)) {
    const sets = fs.readdirSync(m1Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m1Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        await validateM1(path.join(m1Dir, set, file), `mondai1/${set}/${file}`);
      }
    }
  }

  // Quét M2
  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        await validateM2(path.join(m2Dir, set, file), `mondai2/${set}/${file}`);
      }
    }
  }

  fs.appendFileSync(REPORT_FILE, `\n--- KẾT LUẬN ---\nTổng số câu đã check: ${totalChecked}\nTổng số lỗi phát hiện: ${totalErrors}\n`);
  console.log(`\nHoàn tất quét! Đã check ${totalChecked} câu. Phát hiện ${totalErrors} lỗi.`);
  console.log(`Chi tiết lỗi đã được ghi vào file: ${REPORT_FILE}`);
}

run().catch(console.error);
