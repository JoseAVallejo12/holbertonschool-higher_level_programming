#!/usr/bin/node
/* Write a script that prints a square */
const squareSize = parseInt(process.argv[2], 10);
const txt = 'X';
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    console.log(txt.repeat(squareSize));
  }
}
