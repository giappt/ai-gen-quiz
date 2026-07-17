import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import csvParser from 'csv-parser';
import { createObjectCsvWriter } from 'csv-writer';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

const ADVERBS = ['まもなく', '完全に', 'もっと早く', '何度も', '少し', 'ちょっと', 'よく', 'いつも', 'ずっと', '必ず', 'もっと', 'もう', 'まだ', '決して', 'どうしても', 'たぶん', 'きっと', 'すぐ', 'すぐに', '急に', 'たまに', 'ぜひ', '絶対に', '非常に', 'とても', '大変', 'かなり', '大いに', 'すっかり'];

// Particles to split on
const PARTICLES = ['は', 'が', 'を', 'に', 'で', 'と', 'へ', 'や', 'も', 'の', 'て', 'で', 'から', 'まで'];

function splitChunk(chunk) {
    if (!chunk || chunk.length < 2) return null;
    
    // 1. Try to split after a particle, but ensure there is something after it
    // E.g., "日本の歴史" -> "日本の", "歴史"
    for (let p of PARTICLES) {
        let idx = chunk.indexOf(p);
        if (idx > 0 && idx < chunk.length - p.length) {
            return [chunk.substring(0, idx + p.length), chunk.substring(idx + p.length)];
        }
    }
    
    // 2. Try splitting kanji to hiragana transition
    // E.g., "食べる" -> "食べ", "る"
    for (let i = 1; i < chunk.length - 1; i++) {
        const isKanji = chunk.charCodeAt(i-1) >= 0x4e00 && chunk.charCodeAt(i-1) <= 0x9faf;
        const isHiragana = chunk.charCodeAt(i) >= 0x3040 && chunk.charCodeAt(i) <= 0x309f;
        if (isKanji && isHiragana) {
            return [chunk.substring(0, i), chunk.substring(i)];
        }
    }
    
    // 3. Just split in half as a last resort
    const mid = Math.floor(chunk.length / 2);
    return [chunk.substring(0, mid), chunk.substring(mid)];
}

async function fixAdverbs() {
    const flaggedFile = path.join(BASE_DIR, 'flagged_all.json');
    if (!fs.existsSync(flaggedFile)) {
        console.error("flagged_all.json not found!");
        return;
    }

    const flagged = JSON.parse(fs.readFileSync(flaggedFile, 'utf8'));
    // Filter to just N5 LOOSE_ADVERB
    const n5Adverbs = flagged.filter(x => x.file.includes('set_5_jlpt_exam') && x.type === 'LOOSE_ADVERB');
    
    console.log(`Attempting to auto-fix ${n5Adverbs.length} N5 loose adverbs...`);
    
    // Group by file
    const byFile = {};
    for (const item of n5Adverbs) {
        if (!byFile[item.file]) byFile[item.file] = [];
        byFile[item.file].push(item);
    }
    
    let fixCount = 0;
    
    for (const [relPath, items] of Object.entries(byFile)) {
        const filePath = path.join(BASE_DIR, relPath);
        if (!fs.existsSync(filePath)) continue;
        
        const rows = await new Promise((resolve, reject) => {
            const results = [];
            fs.createReadStream(filePath)
              .pipe(csvParser({ mapHeaders: ({ header }) => header.trim().replace(/^\uFEFF/, '') }))
              .on('data', (data) => results.push(data))
              .on('end', () => resolve(results))
              .on('error', reject);
        });
        
        let fixed = false;
        for (const item of items) {
            const rowIdx = item.row - 2;
            const row = rows[rowIdx];
            if (!row) continue;
            
            const chunks = [row.Chunk1, row.Chunk2, row.Chunk3, row.Chunk4];
            const advIdx = chunks.findIndex(c => c === item.adverb);
            if (advIdx === -1) continue;
            
            // We want to lock the adverb.
            // If it's C1, merge to Prefix.
            // If it's C4, merge to Suffix.
            // Otherwise merge into Prefix or Suffix based on proximity.
            let targetChunkToSplit = -1;
            
            if (advIdx === 0) {
                row.Prefix = (row.Prefix || '') + row.Chunk1;
                chunks[0] = null; // empty it
                targetChunkToSplit = 1; // Try splitting C2
            } else if (advIdx === 3) {
                row.Suffix = row.Chunk4 + (row.Suffix || '');
                chunks[3] = null;
                targetChunkToSplit = 2; // Try splitting C3
            } else if (advIdx === 1) {
                row.Prefix = (row.Prefix || '') + row.Chunk1 + row.Chunk2;
                chunks[0] = null;
                chunks[1] = null;
                // Need to split 2 chunks? This is getting complicated.
                // Let's just merge it to the PREVIOUS chunk.
                chunks[0] = chunks[0] + chunks[1];
                chunks[1] = null;
                targetChunkToSplit = 0;
            } else if (advIdx === 2) {
                // Merge C3 to C4
                chunks[3] = chunks[2] + chunks[3];
                chunks[2] = null;
                targetChunkToSplit = 3;
            }
            
            // Actually, a universally safer strategy:
            // Find a chunk to split.
            // Put the adverb together with another chunk.
            
            // Simplified Strategy:
            // Remove adverb. We have 3 chunks left.
            const remaining = chunks.filter((c, i) => i !== advIdx);
            
            // Merge the adverb into Prefix
            if (advIdx <= 1) {
                row.Prefix = (row.Prefix || '');
                // But wait, order matters!
            }
            
            // Let's do it right: We merge the Adverb into its ADJACENT left text or right text.
            // If it's C1, it's next to Prefix.
            let success = false;
            if (advIdx === 0) {
                row.Prefix = (row.Prefix || '') + chunks[0];
                const splitted = splitChunk(chunks[1]);
                if (splitted) {
                    row.Chunk1 = splitted[0];
                    row.Chunk2 = splitted[1];
                    row.Chunk3 = chunks[2];
                    row.Chunk4 = chunks[3];
                    success = true;
                }
            } else if (advIdx === 3) {
                row.Suffix = chunks[3] + (row.Suffix || '');
                const splitted = splitChunk(chunks[2]);
                if (splitted) {
                    row.Chunk1 = chunks[0];
                    row.Chunk2 = chunks[1];
                    row.Chunk3 = splitted[0];
                    row.Chunk4 = splitted[1];
                    success = true;
                }
            } else if (advIdx === 1) {
                // Merge C1 and C2 (Adverb)
                const splitted = splitChunk(chunks[0] + chunks[1]);
                if (splitted) {
                    row.Chunk1 = splitted[0];
                    row.Chunk2 = splitted[1];
                    row.Chunk3 = chunks[2];
                    row.Chunk4 = chunks[3];
                    success = true;
                } else {
                    const split2 = splitChunk(chunks[2]);
                    if (split2) {
                        row.Chunk1 = chunks[0] + chunks[1];
                        row.Chunk2 = split2[0];
                        row.Chunk3 = split2[1];
                        row.Chunk4 = chunks[3];
                        success = true;
                    }
                }
            } else if (advIdx === 2) {
                const splitted = splitChunk(chunks[2] + chunks[3]);
                if (splitted) {
                    row.Chunk1 = chunks[0];
                    row.Chunk2 = chunks[1];
                    row.Chunk3 = splitted[0];
                    row.Chunk4 = splitted[1];
                    success = true;
                }
            }
            
            if (success) {
                row['Original Example'] = (row['Prefix'] || '') + (row['Chunk1'] || '') + (row['Chunk2'] || '') + (row['Chunk3'] || '') + (row['Chunk4'] || '') + (row['Suffix'] || '');
                fixed = true;
                fixCount++;
            }
        }
        
        if (fixed) {
            const headers = Object.keys(rows[0]);
            const csvWriter = createObjectCsvWriter({
                path: filePath,
                header: headers.map(h => ({ id: h, title: h }))
            });
            await csvWriter.writeRecords(rows);
        }
    }
    
    console.log(`Successfully auto-fixed ${fixCount} loose adverbs in N5.`);
}

fixAdverbs().catch(console.error);
