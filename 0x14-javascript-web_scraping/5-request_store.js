#!/usr/bin/node
/* script that gets the contents of a webpage and
stores it in a file. http://loripsum.net/api loripsum */
const fs = require('fs');
const request = require('request');

request.get({ url: process.argv[2] }, (err, res, body) => {
  if (err) console.log(err);
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) console.log(err);
  });
});
