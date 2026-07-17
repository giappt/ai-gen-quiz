import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const ADVERBS = ['まもなく', '完全に', 'もっと早く', '何度も', '少し', 'ちょっと', 'よく', 'いつも', 'ずっと', '必ず', 'もっと', 'もう', 'まだ', '決して', 'どうしても', 'たぶん', 'きっと', 'すぐ', 'すぐに', '急に', 'たまに', 'ぜひ', '絶対に', '非常に', 'とても', '大変', 'かなり', '大いに', 'すっかり'];

function getFiles(dir, filesList = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            getFiles(fullPath, filesList);
        } else if (fullPath.endsWith('.csv')) {
            filesList.push(fullPath);
        }
    }
    return filesList;
}

async function scanFiles() {
    const csvFiles = getFiles(path.join(BASE_DIR, 'mondai2_ordering', 'csv_filled'));
    const flagged = [];
    let fileCount = 0;

    for (const filePath of csvFiles) {
        fileCount++;
        const relativePath = path.relative(BASE_DIR, filePath).replace(/\\/g, '/');
        
        const rows = await new Promise((resolve, reject) => {
            const results = [];
            fs.createReadStream(filePath)
              .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
              .on('data', (data) => results.push(data))
              .on('end', () => resolve(results))
              .on('error', reject);
        });

        rows.forEach((r, i) => {
            const chunks = [r.Chunk1, r.Chunk2, r.Chunk3, r.Chunk4].map(c => c ? c.trim() : '');
            if (chunks.some(c => c === '')) return;

            // 1. Duplicate chunks
            const unique = new Set(chunks);
            if (unique.size < 4) {
                flagged.push({
                    file: relativePath, row: i + 2, type: 'DUPLICATE',
                    original: r['Original Example'],
                    chunks
                });
                return;
            }

            // 2. Loose Adverbs (Chunk is EXACTLY an adverb)
            const looseAdverb = chunks.find(c => ADVERBS.includes(c));
            if (looseAdverb) {
                flagged.push({
                    file: relativePath, row: i + 2, type: 'LOOSE_ADVERB', adverb: looseAdverb,
                    original: r['Original Example'],
                    chunks,
                    p: r.Prefix, s: r.Suffix
                });
            }
        });
    }

    fs.writeFileSync(path.join(BASE_DIR, 'flagged_all.json'), JSON.stringify(flagged, null, 2));
    console.log(`Scan complete. Processed ${fileCount} files. Found ${flagged.length} suspicious rows.`);
}

scanFiles().catch(console.error);
