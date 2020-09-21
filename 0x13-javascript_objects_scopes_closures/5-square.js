#!/usr/bin/node
/* that defines a square and inherits from Rectangle
constructor must take 1 argument: size
constructor of Rectangle must be called (by using super()) */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
