#!/usr/bin/node
const apiUrl = process.argv.slice(2)[0];
const request = require('request');

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const result = {};
    const parseData = JSON.parse(body);
    parseData.forEach(item => {
      if (item.completed) {
        if (result[item.userId] === undefined) {
          result[item.userId] = 1;
        } else result[item.userId] += 1;
      }
    });
    console.log(result);
  }
});
