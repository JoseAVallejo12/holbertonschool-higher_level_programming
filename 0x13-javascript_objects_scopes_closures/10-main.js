#!/usr/bin/node
const converter = require('./10-converter').converter;

console.log('convert decimal 2, 12, 89 to decimal');
let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

console.log('convert decimal 2, 12, 89 to hex');
myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

console.log('convert decimal 2, 12, 89 to octal');
myConverter = converter(8);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
