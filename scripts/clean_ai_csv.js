import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const BASE_DIR = path.join(__dirname, '..');

// Hàm loại bỏ dấu ngoặc kép hoặc ngoặc vuông thừa ở đầu và cuối chuỗi (ví dụ: "「...」")
function cleanCell(field) {
  if (!field) return '';
  let cleaned = String(field).trim();
  // Strip enclosing quotes
  if (cleaned.startsWith('「') && cleaned.endsWith('」')) {
    cleaned = cleaned.slice(1, -1);
  }
  // Strip stray leading/trailing quotes (often found in Prefix/Suffix)
  if (cleaned.startsWith('「')) cleaned = cleaned.slice(1).trim();
  if (cleaned.endsWith('」')) cleaned = cleaned.slice(0, -1).trim();
  return cleaned;
}

function escapeCSV(field) {
  if (field === null || field === undefined) return '';
  const stringField = String(field);
  if (stringField.includes(',') || stringField.includes('"') || stringField.includes('\n')) {
    return `"${stringField.replace(/"/g, '""')}"`;
  }
  return stringField;
}

async function processType(typeFolder) {
  const templatesBase = path.join(BASE_DIR, typeFolder, 'csv_templates');
  const filledBase = path.join(BASE_DIR, typeFolder, 'csv_filled');
  const cleanedBase = path.join(BASE_DIR, typeFolder, 'csv_cleaned');

  if (!fs.existsSync(filledBase)) {
    console.log(`Bỏ qua ${typeFolder} vì chưa có thư mục csv_filled.`);
    return;
  }

  const sets = fs.readdirSync(filledBase).filter(f => !f.includes('.'));
  
  for (const setFolder of sets) {
    const setTemplatesDir = path.join(templatesBase, setFolder);
    const setFilledDir = path.join(filledBase, setFolder);

    const files = fs.readdirSync(setFilledDir).filter(f => f.endsWith('.csv'));
    
    for (const file of files) {
      const origPath = path.join(setTemplatesDir, file);
      const fillPath = path.join(setFilledDir, file);
      const cleanPath = fillPath; // Overwrite directly into csv_filled

      if (!fs.existsSync(origPath)) {
        console.warn(`Cảnh báo: Không tìm thấy file gốc ${origPath}`);
        continue;
      }

      try {
        const origRows = await readCSV(origPath);
        const fillRows = await readCSV(fillPath);

        if (origRows.length !== fillRows.length) {
          console.warn(`LỆCH DÒNG tại ${typeFolder}/${setFolder}/${file}: Gốc=${origRows.length}, Filled=${fillRows.length}`);
        }

        // Lấy headers từ file gốc
        if (origRows.length === 0) continue;
        const headers = Object.keys(origRows[0]);
        let csvContent = '\uFEFF';
        csvContent += headers.map(escapeCSV).join(',') + '\n';

        const maxLen = Math.min(origRows.length, fillRows.length);
        for (let i = 0; i < maxLen; i++) {
          const orig = origRows[i];
          const fill = fillRows[i];
          const row = [];

          for (const header of headers) {
            // 4 cột đầu tiên luôn lấy cứng từ Template gốc để tránh sai lệch khóa học
            if (['Grammar', 'Usage', 'JLPT Level', 'Reference Example'].includes(header)) {
              row.push(escapeCSV(orig[header] || ''));
            } else {
              // Các cột còn lại lấy từ file Filled của Claude, đồng thời clean dấu ngoặc kép/vuông thừa
              row.push(escapeCSV(cleanCell(fill[header])));
            }
          }
          csvContent += row.join(',') + '\n';
        }

        fs.writeFileSync(cleanPath, csvContent, 'utf8');
        console.log(`✅ Đã dọn dẹp và đồng bộ: ${typeFolder}/${setFolder}/${file}`);
      } catch (err) {
        console.error(`❌ Lỗi khi xử lý ${file}:`, err);
      }
    }
  }
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
  console.log("Bắt đầu dọn dẹp và đồng bộ dữ liệu AI-Gen...");
  await processType('mondai1_fill_blank');
  await processType('mondai2_ordering');
  console.log("HOÀN TẤT!");
}

run().catch(console.error);
