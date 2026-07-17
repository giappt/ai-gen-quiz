import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

async function fixFile(relativePath, updateFn) {
    const filePath = path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled', relativePath);
    if (!fs.existsSync(filePath)) return;

    const rows = await new Promise((resolve, reject) => {
        const results = [];
        fs.createReadStream(filePath)
          .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
          .on('data', (data) => results.push(data))
          .on('end', () => resolve(results))
          .on('error', reject);
    });

    let headers = Object.keys(rows[0]);
    let fixed = false;

    rows.forEach((row, i) => {
        if (updateFn(row, i)) {
            row['Original Example'] = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
            fixed = true;
        }
    });

    if (fixed) {
        const csvWriter = createObjectCsvWriter({
            path: filePath,
            header: headers.map(h => ({ id: h, title: h }))
        });
        await csvWriter.writeRecords(rows);
    }
}

async function run() {
    await fixFile('set_5_jlpt_exam/part_98.csv', (row, i) => {
        if (i === 4) {
            // もの (N4) 論文を書くときは...
            row['Prefix'] = '論文を';
            row['Chunk1'] = '書くときは、';
            row['Chunk2'] = '論理的にものを';
            row['Chunk3'] = '言う';
            row['Chunk4'] = '必要が';
            row['Suffix'] = 'ある。';
            return true;
        }
        if (i === 5) {
            // 近代の哲学者たちは...
            row['Prefix'] = '近代の哲学者たちは、生涯かけて';
            row['Chunk1'] = '真理';
            row['Chunk2'] = 'という';
            row['Chunk3'] = 'ものを';
            row['Chunk4'] = '追い';
            row['Suffix'] = '求めた。';
            return true;
        }
        if (i === 6) {
            // 学術的な研究というものは...
            row['Prefix'] = '学術的な研究';
            row['Chunk1'] = 'という';
            row['Chunk2'] = 'ものは、';
            row['Chunk3'] = '客観的な分析が';
            row['Chunk4'] = '不可欠';
            row['Suffix'] = 'である。';
            return true;
        }
        if (i === 7) {
            // どんなに懇願しても... (Duplicate chunks issue)
            row['Prefix'] = 'どんなに懇願しても、学則で許可されない';
            row['Chunk1'] = 'ものは';
            row['Chunk2'] = '決して';
            row['Chunk3'] = '許可';
            row['Chunk4'] = 'されない。';
            row['Suffix'] = '';
            row['Explanation'] = 'Vế đầu là mệnh đề nhượng bộ. Trợ từ `ものは` thay thế cho đối tượng bị cấm đoán. Cụm phó từ `決して` (tuyệt đối không) đứng trước động từ thể bị động phủ định `許可されない` để nhấn mạnh sự từ chối ở cuối câu. Thứ tự chuẩn xác 1-2-3-4.';
            return true;
        }
        if (i === 8) {
            // Broken sentence at the end
            row['Prefix'] = '「どうして試験の';
            row['Chunk1'] = '準備を';
            row['Chunk2'] = 'しなかった';
            row['Chunk3'] = 'のですか」「時間が';
            row['Chunk4'] = 'なかったんだもの。」';
            row['Suffix'] = '';
            row['Explanation'] = 'Câu hỏi sử dụng phó từ nghi vấn `どうして` đi kèm tân ngữ `準備を` và động từ quá khứ `しなかったのですか` (sao lại không chuẩn bị?). Câu trả lời đưa ra lý do chủ quan với `時間がなかった` kết hợp với đuôi giải thích mang tính biện bạch `んだもの`.';
            return true;
        }
        return false;
    });
}

run().catch(console.error);
