#!/usr/bin/node
/*  Script that prints the number of movies
where the character “Wedge Antilles” is present. */
const request = require('request');
request.get({ url: process.argv[2], json: true },
  function (err, res, body) {
    if (err) console.log(err);
    const resultsList = body.results;
    let characterCount = 0;
    for (const index in resultsList) {
      const peoplesApiList = resultsList[index].characters;
      for (const idx in peoplesApiList) {
        if (peoplesApiList[idx].match('18')) {
          characterCount += 1;
        }
      }
    }
    console.log(characterCount);
  });
