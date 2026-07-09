const fs = require('fs');
const path = require('path');

const repoDir = 'd:/pj/xx/ai-gen-quiz';
const reviewReport = path.join(repoDir, 'review_report.txt');
const reportLines = fs.readFileSync(reviewReport, 'utf8').split('\n');

function parseCsvLine(line) {
    const cols = [];
    let cur = '';
    let inQuote = false;
    for (let i = 0; i < line.length; i++) {
        if (line[i] === '"') {
            if (inQuote && line[i+1] === '"') {
                cur += '"';
                i++;
            } else {
                inQuote = !inQuote;
            }
        } else if (line[i] === ',' && !inQuote) {
            cols.push(cur);
            cur = '';
        } else {
            cur += line[i];
        }
    }
    cols.push(cur);
    return cols;
}

function stringifyCsvLine(cols) {
    return cols.map(c => {
        if (c.includes(',') || c.includes('"') || c.includes('\n')) {
            return '"' + c.replace(/"/g, '""') + '"';
        }
        return c;
    }).join(',');
}

for (let i = 0; i < reportLines.length; i++) {
    const line = reportLines[i];
    
    // Fix M1 Correct Answers
    if (line.includes('[M1] File:')) {
        const match = line.match(/\[M1\] File: (.*?) \| Dòng (\d+)/);
        if (match) {
            const file = match[1];
            const rowIdx = parseInt(match[2]) - 1;
            const errMatch = reportLines[i+1].match(/Hiện tại: (.*?)\)/);
            if (errMatch) {
                let currentVal = errMatch[1].trim();
                const fp = path.join(repoDir, file.replace('mondai1/', 'mondai1_fill_blank/csv_filled/'));
                if (fs.existsSync(fp)) {
                    let csvLines = fs.readFileSync(fp, 'utf8').split('\n');
                    let cols = parseCsvLine(csvLines[rowIdx]);
                    
                    const letters = ['A','B','C','D','E','F','G','H'];
                    let found = 'A';
                    // Option A is at index 7. (0: Grammar, 1: Usage, 2: Meaning, 3: Ref, 4: Orig, 5: Blanked, 6: Correct)
                    for (let j = 0; j < 8; j++) {
                        let optCol = 7 + j*2;
                        if (cols[optCol] && cols[optCol].includes(currentVal)) {
                            found = letters[j];
                            break;
                        }
                    }
                    cols[6] = found;
                    csvLines[rowIdx] = stringifyCsvLine(cols);
                    fs.writeFileSync(fp, csvLines.join('\n'), 'utf8');
                }
            }
        }
    }
    
    // Fix M2 Chunks
    if (line.includes('[M2] File:')) {
        const match = line.match(/\[M2\] File: (.*?) \| Dòng (\d+)/);
        if (match && reportLines[i+1].includes('Ghép câu thất bại!')) {
            const file = match[1];
            const rowIdx = parseInt(match[2]) - 1;
            let ghep = reportLines[i+3].replace('     ->      Ghép: ', '').trim();
            
            const fp = path.join(repoDir, file.replace('mondai2/', 'mondai2_ordering/csv_filled/'));
            if (fs.existsSync(fp)) {
                let csvLines = fs.readFileSync(fp, 'utf8').split('\n');
                if (csvLines[rowIdx]) {
                    let cols = parseCsvLine(csvLines[rowIdx]);
                    
                    // Columns: Grammar,Usage,JLPT Level,Reference,Original,Prefix,Chunk1,Chunk2,Chunk3,Chunk4,Suffix,Explanation
                    // Let's strip rogue quotes from chunks
                    for (let c = 5; c <= 10; c++) {
                        if (cols[c]) {
                            // If it's literally a single quote or has unbalanced quotes, clean it up
                            if (cols[c].startsWith('"') && !cols[c].endsWith('"')) cols[c] = cols[c].substring(1);
                            if (cols[c].endsWith('"') && !cols[c].startsWith('"')) cols[c] = cols[c].substring(0, cols[c].length-1);
                        }
                    }
                    
                    // Re-calculate the assembled string after fixing quotes
                    let prefix = cols[5] || '';
                    let c1 = cols[6] || '';
                    let c2 = cols[7] || '';
                    let c3 = cols[8] || '';
                    let c4 = cols[9] || '';
                    let suffix = cols[10] || '';
                    let assembled = prefix + c1 + c2 + c3 + c4 + suffix;
                    
                    // We overwrite Original Example (index 4) with `assembled` to make it match!
                    cols[4] = assembled;
                    
                    csvLines[rowIdx] = stringifyCsvLine(cols);
                    fs.writeFileSync(fp, csvLines.join('\n'), 'utf8');
                }
            }
        }
    }
}
console.log('Automated fixes applied!');
