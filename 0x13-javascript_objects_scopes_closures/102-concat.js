#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  const [file1, file2, file3] = process.argv;

  fs.readFile(file1, (err, content) => {
    if (err) throw err;
    fs.readFile(file2, (err, content2) => {
      if (err) throw err;

      content = Buffer.concat([content, content2]);
      fs.writeFile(file3, content, (err) => {
        if (err) throw err;
      });
    });
  });
}
