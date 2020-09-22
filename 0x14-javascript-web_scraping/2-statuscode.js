#!/usr/bin/node
/* Write a script that display the status code of a GET request. */
const request = require('request');
request.get(process.argv[2], (error, res, body) => {
  const sms = `code: ${res.statusCode}`;
  console.log(sms);
});
