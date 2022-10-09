#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
request(args[0], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(args[1], body, 'utf8', (error) => {
      if (error) console.log(error);
    });
  }
});
