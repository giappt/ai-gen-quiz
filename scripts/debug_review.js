import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const errorsToLog = [
  { file: 'mondai2/set_1_daily/part_67.csv', line: 7 },
  { file: 'mondai2/set_1_daily/part_67.csv', line: 9 },
  { file: 'mondai2/set_1_daily/part_72.csv', line: 21 },
  { file: 'mondai2/set_1_daily/part_86.csv', line: 3 },
  { file: 'mondai2/set_1_daily/part_91.csv', line: 13 },
  { file: 'mondai2/set_2_business/part_10.csv', line: 3 },
  { file: 'mondai2/set_2_business/part_7.csv', line: 10 }
];

async function run() {
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_cleaned');
  
  for (const err of errorsToLog) {
    const parts = err.file.split('/');
    const filePath = path.join(m2Dir, parts[1], parts[2]);
    if (!fs.existsSync(filePath)) continue;
    
    const rows = await new Promise((resolve, reject) => {
      const results = [];
      fs.createReadStream(filePath)
        .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
        .on('data', (data) => results.push(data))
        .on('end', () => resolve(results))
        .on('error', reject);
    });
    
    const row = rows[err.line - 2]; // lineNum = index + 2 => index = lineNum - 2
    console.log(`\n--- ${err.file} | Dòng ${err.line} ---`);
    if (row) {
      console.log(`Prefix: [${row['Prefix']}]`);
      console.log(`Chunk1: [${row['Chunk1']}]`);
      console.log(`Chunk2: [${row['Chunk2']}]`);
      console.log(`Chunk3: [${row['Chunk3']}]`);
      console.log(`Chunk4: [${row['Chunk4']}]`);
      console.log(`Suffix: [${row['Suffix']}]`);
      console.log(`Explanation: [${row['Explanation']}]`);
    } else {
      console.log("ROW NOT FOUND");
    }
  }
}

run().catch(console.error);
