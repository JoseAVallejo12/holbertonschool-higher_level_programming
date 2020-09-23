#!/usr/bin/node
/* script that prints all characters of a Star Wars movie: */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function name (list, idx) {
  request.get({ url: list[idx], json: true }, (err, res) => {
    if (err) console.log(err);
    console.log(res.body.name);
    if (idx + 1 < list.length) {
      name(list.shift(), idx++);
    }
  });
}

request.get({ url: url, json: true }, function (err, res, body) {
  if (err) console.log(err);
  console.log(body.characters);
  name(body.characters, 0);
});
