#!/usr/bin/node
/* script that prints all characters of a Star Wars movie: */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get({ url: url, json: true },
  function (err, res, body) {
    if (err) console.log(err);
    body.characters.forEach(element => {
      request.get({ url: element, json: true }, (err, res) => {
        if (err) console.log(err);
        console.log(res.body.name);
      });
    });
  });
