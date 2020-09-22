#!/usr/bin/node
/* Write a script that prints the title of a Star
Wars movie where the episode number matches a given integer. */
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (err, res, body) {
    if (err) console.log(err);
    console.log(JSON.parse(body).title);
  });
