#!/usr/bin/node
/* Write a script that reads and prints the content of a file. */
var fs = require('fs');

fs.readFile('./' + process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
