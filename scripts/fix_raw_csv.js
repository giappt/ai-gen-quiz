import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

function fixCsvContent(content) {
  // The mangled pattern looks like:
  // ,"""Chunk1"",""Chunk2"",""Chunk3"",""Chunk4"",""Suffix"",""Explanation""""\n
  // We want to replace it with:
  // ,"Chunk1","Chunk2","Chunk3","Chunk4","Suffix","Explanation"\n
  
  // Regex explanation:
  // ,""" matches the start of the mangled chunk1
  // (.*?)"","" matches chunk1
  // (.*?)"","" matches chunk2
  // (.*?)"","" matches chunk3
  // (.*?)"","" matches chunk4
  // (.*?)"","" matches suffix
  // (.*?)""""(?:\r?\n|$) matches explanation and the end of the line
  
  const regex = /,"""(.*?)"",""(.*?)"",""(.*?)"",""(.*?)"",""(.*?)"",""([\s\S]*?)""""(\r?\n|$)/g;
  
  let fixedContent = content.replace(regex, (match, c1, c2, c3, c4, s, exp, newline) => {
    // Return properly formatted CSV columns
    return `,"${c1}","${c2}","${c3}","${c4}","${s}","${exp}"${newline}`;
  });

  // Also fix the case where the original example has an unclosed quote, e.g.,
  // Moscato,""新しいスマホを買う...らない。",新しい
  // We'll just replace ,"" with ,"
  // Wait, if it's ,""新しい... it means it starts with "" which is invalid.
  // Let's fix ,"" at the start of a field:
  fixedContent = fixedContent.replace(/,""/g, ',"');

  return fixedContent;
}

function processAll() {
  const m2Dir = path.join(BASE_DIR, 'mondai2_ordering', 'csv_cleaned');
  let fixedFiles = 0;
  if (fs.existsSync(m2Dir)) {
    const sets = fs.readdirSync(m2Dir).filter(f => !f.includes('.'));
    for (const set of sets) {
      const files = fs.readdirSync(path.join(m2Dir, set)).filter(f => f.endsWith('.csv'));
      for (const file of files) {
        const filePath = path.join(m2Dir, set, file);
        const originalContent = fs.readFileSync(filePath, 'utf8');
        const newContent = fixCsvContent(originalContent);
        if (originalContent !== newContent) {
          fs.writeFileSync(filePath, newContent, 'utf8');
          fixedFiles++;
          console.log(`Fixed raw CSV: ${file}`);
        }
      }
    }
  }
  console.log(`Finished fixing raw CSVs. Fixed ${fixedFiles} files.`);
}

processAll();
