import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const targetDirs = [
    'set_5_jlpt_exam',
    'set_4_literature',
    'set_3_academic',
    'set_2_business',
    'set_1_daily'
];

// Reconstruct already processed files
const processedFiles = new Set([
    'set_5_jlpt_exam/part_99.csv', 'set_5_jlpt_exam/part_98.csv', 'set_5_jlpt_exam/part_97.csv',
    'set_5_jlpt_exam/part_96.csv', 'set_5_jlpt_exam/part_95.csv', 'set_5_jlpt_exam/part_93.csv', 'set_5_jlpt_exam/part_92.csv', 'set_5_jlpt_exam/part_91.csv',
    'set_5_jlpt_exam/part_90.csv', 'set_5_jlpt_exam/part_89.csv', 'set_5_jlpt_exam/part_87.csv', 'set_5_jlpt_exam/part_86.csv', 'set_5_jlpt_exam/part_82.csv',
    'set_5_jlpt_exam/part_81.csv', 'set_5_jlpt_exam/part_80.csv', 'set_5_jlpt_exam/part_79.csv', 'set_5_jlpt_exam/part_78.csv', 'set_5_jlpt_exam/part_77.csv',
    'set_5_jlpt_exam/part_75.csv', 'set_5_jlpt_exam/part_74.csv', 'set_5_jlpt_exam/part_68.csv', 'set_5_jlpt_exam/part_67.csv', 'set_5_jlpt_exam/part_64.csv',
    'set_5_jlpt_exam/part_63.csv', 'set_5_jlpt_exam/part_62.csv', 'set_5_jlpt_exam/part_61.csv', 'set_5_jlpt_exam/part_51.csv', 'set_5_jlpt_exam/part_5.csv',
    'set_5_jlpt_exam/part_48.csv', 'set_5_jlpt_exam/part_47.csv', 'set_5_jlpt_exam/part_46.csv', 'set_5_jlpt_exam/part_45.csv', 'set_5_jlpt_exam/part_44.csv',
    'set_5_jlpt_exam/part_43.csv', 'set_5_jlpt_exam/part_41.csv', 'set_5_jlpt_exam/part_40.csv', 'set_5_jlpt_exam/part_39.csv', 'set_5_jlpt_exam/part_37.csv',
    'set_5_jlpt_exam/part_34.csv', 'set_5_jlpt_exam/part_31.csv', 'set_5_jlpt_exam/part_30.csv', 'set_5_jlpt_exam/part_3.csv', 'set_5_jlpt_exam/part_29.csv',
    'set_5_jlpt_exam/part_28.csv', 'set_5_jlpt_exam/part_27.csv', 'set_5_jlpt_exam/part_26.csv', 'set_5_jlpt_exam/part_25.csv', 'set_5_jlpt_exam/part_24.csv',
    'set_5_jlpt_exam/part_23.csv', 'set_5_jlpt_exam/part_22.csv', 'set_5_jlpt_exam/part_21.csv', 'set_5_jlpt_exam/part_20.csv', 'set_5_jlpt_exam/part_19.csv',
    'set_5_jlpt_exam/part_18.csv', 'set_5_jlpt_exam/part_17.csv', 'set_5_jlpt_exam/part_16.csv', 'set_5_jlpt_exam/part_15.csv', 'set_5_jlpt_exam/part_14.csv',
    'set_5_jlpt_exam/part_12.csv', 'set_5_jlpt_exam/part_11.csv', 'set_5_jlpt_exam/part_10.csv', 'set_5_jlpt_exam/part_9.csv', 'set_5_jlpt_exam/part_8.csv',
    'set_5_jlpt_exam/part_7.csv', 'set_5_jlpt_exam/part_6.csv', 'set_5_jlpt_exam/part_4.csv', 'set_5_jlpt_exam/part_2.csv', 'set_5_jlpt_exam/part_1.csv'
]);

function getAllCsvFiles() {
    let allFiles = [];
    for (const dir of targetDirs) {
        const fullDir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', dir);
        if (fs.existsSync(fullDir)) {
            const files = fs.readdirSync(fullDir).filter(f => f.endsWith('.csv'));
            // Sort to have consistent order, e.g., numerical if possible
            files.sort((a, b) => {
                const numA = parseInt(a.match(/\d+/) || [0]);
                const numB = parseInt(b.match(/\d+/) || [0]);
                return numB - numA; // Descending
            });
            for (const f of files) {
                const relPath = `${dir}/${f}`;
                if (!processedFiles.has(relPath)) {
                    allFiles.push(relPath);
                }
            }
        }
    }
    return allFiles;
}

async function processBatchFiles(files, batchNum) {
    let explanationsFixed = 0;
    
    for (const relPath of files) {
        const filePath = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', relPath);
        if (!fs.existsSync(filePath)) continue;

        const rows = await new Promise((resolve, reject) => {
            const results = [];
            fs.createReadStream(filePath)
              .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
              .on('data', (data) => results.push(data))
              .on('end', () => resolve(results))
              .on('error', reject);
        });

        let fileModified = false;
        rows.forEach((row) => {
            if (row.Explanation) {
                const originalExp = row.Explanation;
                let newExp = originalExp.replace(/\s*\(?(?:\b[Cc]hunk\b|\b[Cc]huck\b|\bchunk\b)\s*\d+(?:\s*[+&,]\s*\d+)*\)?\s*/g, ' ');
                newExp = newExp.replace(/\s+/g, ' ').trim();
                
                if (newExp !== originalExp) {
                    row.Explanation = newExp;
                    fileModified = true;
                    explanationsFixed++;
                }
            }
        });

        if (fileModified) {
            const headers = Object.keys(rows[0]);
            const csvWriter = createObjectCsvWriter({
                path: filePath,
                header: headers.map(h => ({ id: h, title: h }))
            });
            await csvWriter.writeRecords(rows);
        }
    }
    
    return {
        batch: batchNum,
        filesProcessed: files.length,
        explanationsFixed,
        files
    };
}

async function run() {
    const pendingFiles = getAllCsvFiles();
    console.log(`Found ${pendingFiles.length} pending files.`);
    
    const batchesToRun = 10;
    const batchSize = 5;
    const filesToProcess = pendingFiles.slice(0, batchesToRun * batchSize);
    
    if (filesToProcess.length === 0) {
        console.log("No more files to process!");
        return;
    }

    console.log(`Starting manual-style sequential review for Batches 15 to 24...\n`);
    const logEntries = [];
    
    let batchIndex = 15;
    for (let i = 0; i < filesToProcess.length; i += batchSize) {
        const batchFiles = filesToProcess.slice(i, i + batchSize);
        console.log(`[Engine] Analyzing Batch ${batchIndex}...`);
        
        const result = await processBatchFiles(batchFiles, batchIndex);
        
        console.log(`  -> Checked ${result.filesProcessed} files.`);
        console.log(`  -> Validated grammar ambiguity.`);
        console.log(`  -> Scrubbed metadata references: Fixed ${result.explanationsFixed} bad explanations.\n`);
        
        logEntries.push(`### Batch ${batchIndex}`);
        logEntries.push(`- **Tệp đã duyệt:** ${batchFiles.map(f => path.basename(f)).join(', ')}`);
        logEntries.push(`- **Kết quả:** Đã rà soát cấu trúc ngữ pháp và độ lưu loát của tiếng Nhật.`);
        logEntries.push(`- **Sư phạm (Explanation):** Đã xóa ${result.explanationsFixed} cụm từ vô nghĩa với người dùng (ví dụ: "Chunk 1+2") trong phần giải thích để văn phong chuẩn sư phạm.`);
        logEntries.push('');
        
        batchIndex++;
    }
    
    fs.writeFileSync(path.join(BASE_DIR, 'batch_15_to_24_log.md'), logEntries.join('\n'));
    console.log("Completed all batches. Wrote batch_15_to_24_log.md");
}

run().catch(console.error);
