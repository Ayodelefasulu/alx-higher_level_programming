#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return;
    }

   /* if (h <= 0) {
      return;
    }*/

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
