import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

async function fixFile(relativePath, rowCondition, rowFix) {
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
        if (rowCondition(row, i)) {
            rowFix(row);
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
    await fixFile('set_2_business/part_94.csv', 
        row => row['Original Example'] && row['Original Example'].includes('新しいオフィスの移転先をめぐって'),
        row => {
            row['Original Example'] = '新しいオフィスの移転先をめぐって、社内で意見が対立している。';
            row['Prefix'] = '新しいオフィスの移転先をめぐって、';
            row['Chunk1'] = '社内で';
            row['Chunk2'] = '意見が';
            row['Chunk3'] = '対立して';
            row['Chunk4'] = 'いる。';
            row['Suffix'] = '';
            row['Explanation'] = "Sắp xếp theo cấu trúc tranh luận quanh một chủ đề: '移転先を' (địa điểm chuyển văn phòng) làm tân ngữ cho giới từ -> 'めぐって' (xoay quanh vấn đề gì đó) để mở ra phạm vi của cuộc tranh luận -> '社内で意見が' (ý kiến trong nội bộ công ty) làm chủ ngữ cho động từ -> '対立している' (đang đối đầu/xung đột lẫn nhau). Đây là một cấu trúc ngữ pháp quan trọng cần ghi nhớ để nắm vững ý nghĩa câu.";
        }
    );

    await fixFile('set_4_literature/part_37.csv', 
        row => row['Original Example'] && row['Original Example'].includes('そこの君、立ち止まりなさい！'),
        row => {
            row['Original Example'] = '「ちょっと、そこの君、立ち止まりなさい！」と刑事は逃げる男に向かって叫んだ。';
            row['Prefix'] = '「ちょっと、';
            row['Chunk1'] = 'そこの君、';
            row['Chunk2'] = '立ち止まりなさい！」';
            row['Chunk3'] = 'と刑事は';
            row['Chunk4'] = '逃げる男に向かって';
            row['Suffix'] = '叫んだ。';
            row['Explanation'] = "\"ちょっと\" ở đây đóng vai trò là thán từ dùng để gọi, gây sự chú ý (Này!, Ê!). Tiếp theo là cụm chỉ đối tượng bị gọi \"そこの君\" (cậu kia) và câu mệnh lệnh \"立ち止まりなさい\" (hãy đứng lại!). Toàn bộ lời thoại được nối bằng \"と\", bổ nghĩa bằng phó từ \"大声で\" (bằng giọng lớn) và kết thúc bằng động từ \"叫んだ\" (đã hét lên).";
        }
    );

    await fixFile('set_4_literature/part_38.csv', 
        row => row['Prefix'] === 'どこ',
        row => {
            row['Original Example'] = '「彼、どこへ行ったの？」「どこって、いつもの古い図書館だよ。」';
            row['Prefix'] = '「彼、どこへ行ったの？」「どこって、';
            row['Chunk1'] = 'いつもの';
            row['Chunk2'] = '古い図書館';
            row['Chunk3'] = 'だよ。';
            row['Chunk4'] = '」';
            row['Suffix'] = '';
            row['Explanation'] = "Phân tích cú pháp: 1. Từ nghi vấn 『どこ』 được sử dụng để nhắc lại câu hỏi của người đối thoại. 2. Trợ từ nhấn mạnh 『って』 đóng vai trò hỏi ngược lại hoặc làm rõ chủ đề vừa được nhắc đến (Ý bạn hỏi là 'ở đâu' à?). 3. Định ngữ chỉ thói quen 『いつもの』 bổ nghĩa cho cụm danh từ phía sau. 4. Cụm danh từ 『古い図書館』 kết hợp với hệ từ khẳng định ở Suffix để hoàn thành câu trả lời.";
        }
    );

    await fixFile('set_4_literature/part_67.csv', 
        row => row['Prefix'] && row['Prefix'].includes('なんか'),
        row => {
            row['Original Example'] = '「最近、なんか温かいスープでも飲みたい気分だ」と彼は呟いた。';
            row['Prefix'] = '「最近、なんか';
            row['Chunk1'] = '温かい';
            row['Chunk2'] = 'スープでも';
            row['Chunk3'] = '飲みたい';
            row['Chunk4'] = '気分だ」と';
            row['Suffix'] = '彼は呟いた。';
            row['Explanation'] = "Từ 「なんか」 (hơi hơi/có cảm giác gì đó) đứng đầu bổ nghĩa cho toàn bộ trạng thái cảm xúc. Tiếp theo là tính từ 「温かい」 (ấm áp) bổ nghĩa cho danh từ gợi ý 「スープでも」 (như súp chẳng hạn). Cụm này làm tân ngữ cho động từ muốn 「飲みたい」 (muốn uống).";
        }
    );

    await fixFile('set_4_literature/part_89.csv', 
        row => row['Original Example'] && row['Original Example'].includes('この極秘資料を'),
        row => {
            row['Original Example'] = '「この極秘資料を、しかるべき機関に届けてもらえまいか」と男はかすれた声でささやいた。';
            row['Prefix'] = '「この極秘資料を、しかるべき機関に';
            row['Chunk1'] = '届けて';
            row['Chunk2'] = 'もらえ';
            row['Chunk3'] = 'まいか」と';
            row['Chunk4'] = '男はかすれた声で';
            row['Suffix'] = 'ささやいた。';
            row['Explanation'] = "Mẫu 「V-てもらえまいか」 dùng để đưa ra lời yêu cầu, nhờ vả một cách lịch sự nhưng có phần khẩn thiết trong văn học (với sắc thái mong mỏi đối phương làm gì đó cho mình). Thứ tự kết hợp: tính từ 「しかるべき (thích hợp/phù hợp)」 bổ nghĩa cho danh từ 「機関 (cơ quan)」 -> trợ từ chỉ hướng tới 「に」 -> động từ thể て 「届けて (gửi đến)」 -> thể khả năng của もらう là 「もらえ」 -> phỏng đoán phủ định 「まいか」 biểu thị lời khẩn cầu.";
        }
    );
}

run().catch(console.error);
