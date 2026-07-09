const fs = require('fs');
const lines = fs.readFileSync('d:/pj/xx/ai-gen-quiz/review_report.txt', 'utf8').split('\n');
const errs = lines.filter(l => l.includes('File:'));
console.log('Total errors:', errs.length);
errs.forEach(e => console.log(e));
