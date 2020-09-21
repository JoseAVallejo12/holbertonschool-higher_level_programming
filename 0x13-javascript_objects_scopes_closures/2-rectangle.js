#!/usr/bin/node
/* Class Rectangle. Constructor must take 2 arguments w and h
Initialize instance attribute width, height with the value of w, h
If w or h is equal to 0 or not a positive integer, create an empty object */
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) { return; }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
