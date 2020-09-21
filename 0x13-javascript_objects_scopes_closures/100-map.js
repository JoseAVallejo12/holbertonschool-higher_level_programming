#!/usr/bin/node
/* script that imports an array and computes a new array. */
const { list } = require('./100-data');
const new_list = list.map((idx, value) => idx * value);
console.log(list);
console.log(new_list);
