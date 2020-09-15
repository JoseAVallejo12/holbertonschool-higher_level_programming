#!/usr/bin/node
/* Write a script that prints the addition of 2 integers */

/* add - funtion for add two number
 * @a: number one
 * @b: number two
 * Return: NaN if fail , else int
 */
function add (a, b) {
  const val1 = parseInt(a, 10);
  const val2 = parseInt(b, 10);
  if (isNaN(val1) || isNaN(val2)) {
    return NaN;
  }
  return val1 + val2;
}
console.log(add(process.argv[2], process.argv[3]));
