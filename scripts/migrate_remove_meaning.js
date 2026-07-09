import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const MONDAI2_DIR = path.join(__dirname, '..', 'mondai2_ordering');

// Hàm split chuỗi CSV có bọc ngoặc kép
function splitCSVRow(row) {
    const result = [];
    let current = '';
    let inQuotes = false;
    for (let i = 0; i < row.length; i++) {
        const char = row[i];
        if (char === '"' && row[i + 1] === '"') {
            current += '"';
            i++; // skip escaped quote
        } else if (char === '"') {
            inQuotes = !inQuotes;
        } else if (char === ',' && !inQuotes) {
            result.push(current);
            current = '';
        } else {
            current += char;
        }
    }
    result.push(current);
    return result;
}

function escapeCSV(val) {
    if (val === undefined || val === null) return '';
    const str = String(val);
    if (str.includes(',') || str.includes('"') || str.includes('\n')) {
        return `"${str.replace(/"/g, '""')}"`;
    }
    return str;
}

function processDirectory(dirPath) {
    if (!fs.existsSync(dirPath)) return;
    
    const items = fs.readdirSync(dirPath);
    for (const item of items) {
        const fullPath = path.join(dirPath, item);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory()) {
            processDirectory(fullPath);
        } else if (stat.isFile() && item.endsWith('.csv')) {
            processCSVFile(fullPath);
        }
    }
}

function processCSVFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    if (lines.length === 0 || !lines[0].includes('Meaning')) return; // Already migrated or empty

    let migrated = false;
    const newLines = [];
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;
        
        const cols = splitCSVRow(line);
        // Header check
        if (i === 0) {
            const meaningIndex = cols.indexOf('Meaning');
            if (meaningIndex === -1) {
                console.log(`Bỏ qua ${path.basename(filePath)} (Không có cột Meaning)`);
                return; // Already migrated
            }
        }
        
        // Remove Meaning column (Index 2 in Mondai 2 original schema)
        // Schema: Grammar, Usage, Meaning, Reference Example, ...
        // We assume it's always index 2 based on Mondai 2 headers. Let's strictly delete index 2.
        cols.splice(2, 1);
        
        newLines.push(cols.map(escapeCSV).join(','));
        migrated = true;
    }
    
    if (migrated) {
        fs.writeFileSync(filePath, newLines.join('\n') + '\n', 'utf8');
        console.log(`✅ Đã migrate (xóa cột Meaning): ${path.basename(filePath)}`);
    }
}

console.log("🚀 Bắt đầu quá trình loại bỏ cột Meaning khỏi toàn bộ Mondai 2...");
const dirsToProcess = ['csv_templates', 'csv_filled', 'csv_cleaned'];

for (const subDir of dirsToProcess) {
    const targetPath = path.join(MONDAI2_DIR, subDir);
    if (fs.existsSync(targetPath)) {
        console.log(`\nĐang quét thư mục: ${subDir}...`);
        processDirectory(targetPath);
    }
}
console.log("\n🎉 Đã hoàn tất Migration!");
