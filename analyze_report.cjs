const fs = require('fs');

const lines = fs.readFileSync('review_report.txt', 'utf8').split('\n');
let stats = {
  shortExplain: 0,
  mismatch: 0,
  missingPunctuation: 0,
  files: new Set()
};

let currentFile = null;
for (const line of lines) {
  if (line.startsWith('[M2] File:')) {
    currentFile = line;
    stats.files.add(line.split('|')[0].trim());
  } else if (line.includes('Giải thích quá ngắn')) {
    stats.shortExplain++;
  } else if (line.includes('Ghép câu thất bại')) {
    stats.mismatch++;
  }
}

console.log('Short Explain:', stats.shortExplain);
console.log('Mismatch:', stats.mismatch);
console.log('Files affected:', stats.files.size);
