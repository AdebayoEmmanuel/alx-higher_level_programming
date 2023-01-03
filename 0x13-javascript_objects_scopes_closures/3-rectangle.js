#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0) && (Number.isInteger(w) && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('x'.repeat(this.width));
    }
  }
};
