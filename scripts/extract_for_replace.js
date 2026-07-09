import fs from 'fs';

function extractAndLog(file, pattern) {
  const text = fs.readFileSync(file, 'utf8');
  console.log(`\n=== MATCHES IN ${file} ===`);
  const lines = text.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes(pattern)) {
       console.log(`Line ${i+1}: ${lines[i]}`);
       if (lines[i+1]) console.log(`Line ${i+2}: ${lines[i+1]}`);
       if (lines[i+2]) console.log(`Line ${i+3}: ${lines[i+2]}`);
    }
  }
}

extractAndLog('mondai2_ordering/csv_cleaned/set_1_daily/part_91.csv', '夕食の');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'おいそれと');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'おきに');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'おそれがある');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'おなじ');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'おまけに');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'お思う');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_10.csv', 'おそらく');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_7.csv', 'いっこうに');
extractAndLog('mondai2_ordering/csv_cleaned/set_2_business/part_7.csv', 'いっก็ตาม');
