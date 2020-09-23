#!/usr/bin/node
/* script that computes the number of tasks
completed by user id. The first argument
is the API URL: https://jsonplaceholder.typicode.com/todos */
const request = require('request');
request.get({ url: process.argv[2], json: true }, (err, res, body) => {
  if (err) console.log(err);
  const newObj = {};
  body.forEach((element) => {
    if (element.completed) {
      newObj[element.userId] = newObj[element.userId]
        ? newObj[element.userId] + 1
        : 1;
    }
  });

  console.log(newObj);
});
