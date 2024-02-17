#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function (w, h) {
      let i = 0;
      while (i < this.height) {
        let j = 0;
        while (j < this.width) {
          process.stdout.write('X');
          j++;
        }
        console.log('');
        i++;
      }
    };
  }
}

module.exports = Rectangle;
