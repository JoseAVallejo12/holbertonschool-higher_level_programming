#!/usr/bin/node
/* script that imports an array and computes a new array.
Your script must import list from the file 100-data.js */
const data = require('./100-data');
let idx = 0;
console.log(data.list);
console.log(data.list.map(item => item * (idx++)));
