#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  let [, , file1, file2, file3] = process.argv;
  file1 = fs.readFileSync(file1).toString();
  file2 = fs.readFileSync(file2).toString();
  fs.writeFileSync(file3, file1, file2);
}
