#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0) && (Number.isInteger(w) && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let out = '';
    for (let i = 0; i < this.width; i++) {
      out += 'x';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(out);
    }
  }
};
