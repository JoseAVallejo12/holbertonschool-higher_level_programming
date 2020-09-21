#!/usr/bin/node
/* that defines a square and inherits from Rectangle
constructor must take 1 argument: size
constructor of Rectangle must be called (by using super()) */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let chr = c;
    if (!c) {
      chr = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}
module.exports = Square;
