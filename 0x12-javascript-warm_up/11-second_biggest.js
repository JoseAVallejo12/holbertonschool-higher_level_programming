#!/usr/bin/node
/* Write a script that searches the second biggest integer in the list of arguments. */
const arrNum = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 1; i < process.argv.length; i++) {
    arrNum.push(parseInt(process.argv[i]));
  }
  if ((!arrNum) || (arrNum[0] === 0)) {
    console.log(0);
  } else {
    console.log(
      arrNum.sort((a, b) => {
        return a - b;
      })[arrNum.length - 2]
    );
  }
}
