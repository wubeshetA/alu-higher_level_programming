#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === 'C' || c === 'c') {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
