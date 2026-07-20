const fs = require('fs');
const path = require('path');
const { parse } = require('csv-parse/sync');

const dir = 'd:/pj/xx/ai-gen-quiz/mondai2_ordering/csv_filled/set_4_literature';
const files = ['part_1.csv', 'part_2.csv', 'part_3.csv', 'part_4.csv', 'part_5.csv'];

let output = '';

files.forEach(file => {
    const content = fs.readFileSync(path.join(dir, file), 'utf-8');
    const records = parse(content, { columns: true, skip_empty_lines: true });
    
    output += `# File: ${file}\n\n`;
    records.forEach((record, index) => {
        output += `## ID: ${file}-${index + 1}\n`;
        output += `- **Grammar**: ${record['Grammar']}\n`;
        output += `- **Original Example**: ${record['Original Example']}\n`;
        output += `- **Explanation**: ${record['Explanation']}\n\n`;
    });
});

fs.writeFileSync('d:/pj/xx/ai-gen-quiz/scratch/batch1_review.md', output, 'utf-8');
console.log('Done reading to batch1_review.md');
