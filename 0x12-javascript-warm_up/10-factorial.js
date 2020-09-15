#!/usr/bin/node
/* Write a script that prints the addition of 2 integers */

/* factorial - funtion factorial for a number
 * @a: number
 * Return: Infinity if fail , else int
 */
function factorial (a) {
  let val = 1;
  for (let i = 1; i <= a; i++) {
    val *= i;
  }
  return val;
}
console.log(factorial(process.argv[2]));
