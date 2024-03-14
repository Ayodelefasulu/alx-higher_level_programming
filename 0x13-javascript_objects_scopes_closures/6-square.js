#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  /* constructor (size) {
    super(size);
    this.size = size;
  } */

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
