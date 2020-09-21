#!/usr/bin/node
/* that defines a square and inherits from Rectangle
constructor must take 1 argument: size
constructor of Rectangle must be called (by using super()) */
const square = require("./5-square");

class Square extends square {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    let chr = c;
    if (c === undefined) {
      chr = "X";
    }
    for (let i = 0; i < this.width; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}
module.exports = Square;
