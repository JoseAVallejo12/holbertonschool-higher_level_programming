#!/usr/bin/node
/* Class Rectangle. Constructor must take 2 arguments w and h
Initialize instance attribute width, height with the value of w, h
If w or h is equal to 0 or not a positive integer, create an empty object */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  /* prints the rectangle using the character X */
  print () {
    const chr = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }

  /* exchanges the width and the height of the rectangle */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /* multiples the width and the height of the rectangle by 2 */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
