#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const parseData = JSON.parse(body);
    const results = parseData.results;
    let counter = 0;
    results.forEach(result => {
      result.characters.forEach(characterUrl => {
        if (characterUrl === 'https://swapi-api.hbtn.io/api/people/18/') {
          counter++;
        }
      });
    });
    console.log(counter);
  }
});
