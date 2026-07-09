const fs = require('fs');
const path = require('path');

const repoDir = 'd:/pj/xx/ai-gen-quiz';

function readLines(file) { return fs.readFileSync(path.join(repoDir, file), 'utf8').split('\n'); }
function writeLines(file, lines) { fs.writeFileSync(path.join(repoDir, file), lines.join('\n'), 'utf8'); }

function parseCsvLine(line) {
    const cols = []; let cur = ''; let inQ = false;
    for (let i=0; i<line.length; i++) {
        if (line[i] === '"') {
            if (inQ && line[i+1] === '"') { cur += '"'; i++; }
            else { inQ = !inQ; }
        } else if (line[i] === ',' && !inQ) {
            cols.push(cur); cur = '';
        } else { cur += line[i]; }
    }
    cols.push(cur); return cols;
}

function stringify(cols) {
    return cols.map(c => (c.includes(',')||c.includes('"')||c.includes('\n')) ? `"${c.replace(/"/g, '""')}"` : c).join(',');
}

// 1. Fix M1 part_3 lines 10-20
let m1_3 = readLines('mondai1_fill_blank/csv_filled/set_1_daily/part_3.csv');
for(let i=9; i<=19; i++) {
    if(!m1_3[i]) continue;
    let cols = parseCsvLine(m1_3[i]);
    let target = cols[6];
    let found = 'A';
    for(let j=0; j<8; j++) {
        if(cols[7+j*2] && (cols[7+j*2] === target || cols[7+j*2].includes(target))) {
            found = String.fromCharCode(65+j); break;
        }
    }
    cols[6] = found;
    m1_3[i] = stringify(cols);
}
writeLines('mondai1_fill_blank/csv_filled/set_1_daily/part_3.csv', m1_3);

// 2. Fix M2 Prefix Quotes
const fixPrefixQuote = (file, rows) => {
    let lines = readLines('mondai2_ordering/csv_filled/set_1_daily/' + file);
    rows.forEach(r => {
        if(!lines[r-1]) return;
        let cols = parseCsvLine(lines[r-1]);
        if(cols[5] && cols[5].startsWith('"') && !cols[5].endsWith('"')) cols[5] = cols[5].substring(1);
        if(cols[10] && cols[10].endsWith('"') && !cols[10].startsWith('"')) cols[10] = cols[10].substring(0, cols[10].length-1);
        lines[r-1] = stringify(cols);
    });
    writeLines('mondai2_ordering/csv_filled/set_1_daily/' + file, lines);
};
fixPrefixQuote('part_2.csv', [3, 11, 13]);
fixPrefixQuote('part_23.csv', [3, 10, 18]);
fixPrefixQuote('part_25.csv', [7, 11, 12]);

// 3. Fix M2 Prefix Garbage and Commas
const fixM2 = (file, rowsData) => {
    let lines = readLines('mondai2_ordering/csv_filled/set_1_daily/' + file);
    rowsData.forEach(d => {
        if(!lines[d.row-1]) return;
        let cols = parseCsvLine(lines[d.row-1]);
        if(d.prefix !== undefined) cols[5] = d.prefix;
        if(d.c1 !== undefined) cols[6] = d.c1;
        if(d.c4 !== undefined) cols[9] = d.c4;
        
        let p = cols[5]||''; let c1=cols[6]||''; let c2=cols[7]||''; let c3=cols[8]||''; let c4=cols[9]||''; let s=cols[10]||'';
        cols[4] = p+c1+c2+c3+c4+s; 
        lines[d.row-1] = stringify(cols);
    });
    writeLines('mondai2_ordering/csv_filled/set_1_daily/' + file, lines);
};

fixM2('part_31.csv', [
    {row: 15, prefix: 'そんなに悔しがらないで、'},
    {row: 16, prefix: '仲良くしてよ、'},
    {row: 17, prefix: '駅前のスーパーまでは、'},
    {row: 18, prefix: '朝寝坊した。'},
    {row: 19, prefix: '毎日練習しているんだね。'}
]);
fixM2('part_42.csv', [
    {row: 14, prefix: '家族のために'},
    {row: 16, prefix: '家族が'},
    {row: 19, prefix: '毎日'}
]);
fixM2('part_45.csv', [
    {row: 2, prefix: 'この料理は、'},
    {row: 3, prefix: '私は、'},
    {row: 4, prefix: '誰が'},
    {row: 5, prefix: '昨日のことは、'},
    {row: 6, prefix: ''},
    {row: 7, prefix: 'あの店の商品なら、'},
    {row: 8, prefix: ''},
    {row: 10, prefix: ''},
    {row: 12, prefix: 'このTシャツを買いたいです。'},
    {row: 16, prefix: '彼は'}
]);
fixM2('part_48.csv', [
    {row: 15, c1: '兄が「明日の旅行は中止だ」', c4: '「というと」'}
]);

console.log('Final fixes applied!');
