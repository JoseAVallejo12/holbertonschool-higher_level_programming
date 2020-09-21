#!/usr/bin/node
/* script that imports an array and computes a new array.
Your script must import list from the file 100-data.js */
const { list } = require('./100-data');
let idx = 0;
console.log(list);
console.log(list.map((item) => item * (idx++)));
