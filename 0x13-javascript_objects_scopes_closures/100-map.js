#!/usr/bin/node
/*Script that imports an array and computes a new array. */
const list = require('./100-data').list;
const newList = list.map((index, value) => index * value);
console.log(list);
console.log(newList);
