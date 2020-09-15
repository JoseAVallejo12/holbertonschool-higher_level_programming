#!/usr/bin/node
/* Write a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer: */
const parsed = parseInt(process.argv[2], 10);
if (isNaN(parsed)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsed);
}
