#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  const [file1, file2, file3] = process.argv;

  fs.readFile(file1, (err, content) => {
    if (err) {
      throw err;
    }
    fs.writefile(file3, content);
  });
  fs.readFile(file2, (err, content) => {
    if (err) {
      throw err;
    }
    fs.writefile(file3, content);
  });
}
