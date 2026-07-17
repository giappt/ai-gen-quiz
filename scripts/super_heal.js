import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const vietnameseRegex = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;

// Phép kiểm tra: Chuỗi có phải là tiếng Nhật sạch (chỉ bao gồm ASCII, Punctuation Nhật, Hiragana, Katakana, Kanji, Full-width)
// Không chứa các ký tự có dấu của tiếng Việt hay các ký tự lạ khác.
const isCleanJapanese = (str) => {
    if (!str) return false;
    return /^[\x20-\x7E\u3000-\u303F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF\uFF00-\uFFEF]+$/.test(str);
};

async function processFile(filePath, isM1) {
  const rows = await new Promise((resolve, reject) => {
    const results = [];
    fs.createReadStream(filePath)
      .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
      .on('data', (data) => results.push(data))
      .on('end', () => resolve(results))
      .on('error', reject);
  });

  if (rows.length === 0) return { mismatchFixed: 0, explanationFlagged: 0, chunkFlagged: 0 };

  let mismatchFixed = 0;
  let explanationFlagged = 0;
  let chunkFlagged = 0;
  let hasChanges = false;
  let headers = Object.keys(rows[0]);

  rows.forEach(row => {
    if (!row['Original Example']) return; // Skip empty rows

    if (isM1) {
      // Check Explanations for M1
      const validAnswers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
      for (const opt of validAnswers) {
        if (row[`Option ${opt}`]) {
          const optExpl = row[`Explanation ${opt}`] || '';
          if (!optExpl.includes('[CẦN FIX GIẢI THÍCH]')) {
              if (optExpl.length < 20 || !vietnameseRegex.test(optExpl)) {
                  row[`Explanation ${opt}`] = optExpl + (optExpl.length > 0 ? ' ' : '') + '[CẦN FIX GIẢI THÍCH]';
                  explanationFlagged++;
                  hasChanges = true;
              }
          }
        }
      }
    } else {
      // M2 Checks
      // 1. Missing chunks
      const reqChunks = ['Chunk1', 'Chunk2', 'Chunk3', 'Chunk4'];
      let missingChunk = false;
      for (const ch of reqChunks) {
          if (!row[ch]) {
              row[ch] = '[CẦN FIX]';
              missingChunk = true;
              chunkFlagged++;
              hasChanges = true;
          }
      }

      // 2. Explanation check
      const expl = row['Explanation'] || '';
      if (!expl.includes('[CẦN FIX GIẢI THÍCH]')) {
          if (expl.length < 40 || !vietnameseRegex.test(expl)) {
              row['Explanation'] = expl + (expl.length > 0 ? ' ' : '') + '[CẦN FIX GIẢI THÍCH]';
              explanationFlagged++;
              hasChanges = true;
          }
      }

      // 3. Chunk mismatch
      if (!missingChunk && row['Chunk1']) {
          const original = (row['Original Example'] || '').trim();
          const prefix = (row['Prefix'] || '');
          const c1 = (row['Chunk1'] || '');
          const c2 = (row['Chunk2'] || '');
          const c3 = (row['Chunk3'] || '');
          const c4 = (row['Chunk4'] || '');
          const suffix = (row['Suffix'] || '');
          
          const reconstructed = prefix + c1 + c2 + c3 + c4 + suffix;
          
          if (reconstructed !== original) {
              const normalize = (str) => str.replace(/\s+/g, '').replace(/。/g, '');
              if (normalize(reconstructed) !== normalize(original)) {
                  // Mismatch found. Apply heuristic:
                  if (isCleanJapanese(reconstructed) && !original.includes('[CẦN FIX')) {
                      row['Original Example'] = reconstructed;
                      mismatchFixed++;
                      hasChanges = true;
                  }
              }
          }
      }
    }
  });

  if (hasChanges) {
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
  
  return { mismatchFixed, explanationFlagged, chunkFlagged };
}

async function run() {
  console.log("Bắt đầu thực thi Super Heal (Heuristic Auto-Fix)...");
  
  let totalMismatchFixed = 0;
  let totalExplanationFlagged = 0;
  let totalChunkFlagged = 0;

  const m1Dir = path.join(BASE_DIR, 'mondai1_fill_blank', 'csv_filled');
  if (fs.existsSync(m1Dir)) {
    const sets = fs.readdirSync(m1Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m1Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        const stats = await processFile(path.join(m1Dir, set, file), true);
        totalMismatchFixed += stats.mismatchFixed;
        totalExplanationFlagged += stats.explanationFlagged;
        totalChunkFlagged += stats.chunkFlagged;
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
        totalMismatchFixed += stats.mismatchFixed;
        totalExplanationFlagged += stats.explanationFlagged;
        totalChunkFlagged += stats.chunkFlagged;
      }
    }
  }

  console.log(`\nHoàn tất Super Heal!`);
  console.log(`- Đã vá tự động (ghi đè Original bằng Reconstructed) ${totalMismatchFixed} lỗi Mismatch.`);
  console.log(`- Đã đánh dấu [CẦN FIX GIẢI THÍCH] cho ${totalExplanationFlagged} lỗi giải thích.`);
  console.log(`- Đã đánh dấu [CẦN FIX] cho ${totalChunkFlagged} lỗi thiếu Chunk.`);
  console.log(`\nSếp hãy chạy lại 'npm run review' để xem còn sót bao nhiêu lỗi nhé!`);
}

run().catch(console.error);
