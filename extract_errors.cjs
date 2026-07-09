const fs = require('fs');
const lines = fs.readFileSync('review_report.txt', 'utf8').split('\n');

let currentFile = '';
let currentLine = 0;
let errors = [];
let currentError = null;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (line.startsWith('[M2] File:')) {
    const match = line.match(/File: (.+) \| Dòng (\d+)/);
    if (match) {
      if (currentError) errors.push(currentError);
      currentError = {
        file: match[1],
        row: parseInt(match[2]),
        shortExplain: false,
        goc: '',
        ghep: ''
      };
    }
  } else if (line.includes('Giải thích quá ngắn') && currentError) {
    currentError.shortExplain = true;
  } else if (line.includes('Gốc :') && currentError) {
    currentError.goc = line.split('Gốc :')[1].trim();
  } else if (line.includes('Ghép:') && currentError) {
    currentError.ghep = line.split('Ghép:')[1].trim();
  }
}
if (currentError) errors.push(currentError);

// Group by file
const byFile = {};
errors.forEach(e => {
  if (!byFile[e.file]) byFile[e.file] = [];
  byFile[e.file].push(e);
});

console.log(JSON.stringify(byFile, null, 2));
