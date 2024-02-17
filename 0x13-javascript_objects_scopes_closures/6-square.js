#!/usr/bin/node
const Parent = require('./5-square');

class Square extends Parent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) {
          process.stdout.write(c);
        } else {
          process.stdout.write('X');
        }
      }
    }
  }
}

module.exports = Square;
