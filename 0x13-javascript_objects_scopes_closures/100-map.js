#!/usr/bin/node
/* Script that imports an array and computes a new array. */
const { list } = require('./100-data');
console.log(list);
console.log(list.map((index, value) => index * value));
