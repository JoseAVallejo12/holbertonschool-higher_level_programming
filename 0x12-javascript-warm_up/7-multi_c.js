#!/usr/bin/node
/* Write a script that prints 3 lines:(like 1-multi_languages.js)
but by using an array of string and a loop */
const txt = 'C is fun';
if (!process.argv[2]) console.log('Missing number of occurrences');
for (let i = 0; i < process.argv[2]; i++) {
  console.log(txt);
}
