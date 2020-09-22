#!/usr/bin/node
/* Write a script that reads and prints the content of a file. */
const fs = require('fs');

fs.readFile('./' + process.argv[2], 'utf8', function (err, data) {
  if (err) {
    error = {
        'Error': err.message + ' at Error (native)',
        'errno': err.errno,
        'code': err.code,
        'syscall': err.syscall,
        'path': err.path
    }
    return console.log(error);
  }
  console.log(data);
});
