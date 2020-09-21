#!/usr/bin/node
/* Write a function that executes x times a function.
The function must be visible from outside */
exports.callMeMoby = function (x, cb) {
  for (let i = 0; i < x; i++) {
    cb();
  }
};
