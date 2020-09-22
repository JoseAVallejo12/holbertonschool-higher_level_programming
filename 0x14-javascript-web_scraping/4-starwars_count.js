#!/usr/bin/node
/*  Script that prints the number of movies
where the character “Wedge Antilles” is present. */
const request = require('request');
const url = process.argv[2];
request.get({url:url, json:true},
  function (err, res, body) {
    if (err) console.log(err);
    resultsList = body.results
    characterCount = 0;
    for (const index in resultsList){
        peoplesApiList = resultsList[index].characters;
        for (let idx in peoplesApiList){
            if (peoplesApiList[idx].match('18')){
                characterCount += 1;
            }
        }
    }
    console.log(characterCount);

  });
