#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  const [file1, file2, file3] = process.argv;

  fs.readFile(file1, (err, content1) => {
    if (err) throw err;
    fs.readFile(file2, (err1, content2) => {
      if (err1) throw err1;

      const content = Buffer.concat([content1, content2]);
      fs.writeFile(file3, content, (err2) => {
        if (err2) throw err2;
      });
    });
  });
}
