#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = {};
for (const key in dict) {
  const value = dict[key];
  if (sortedDict[value] === undefined) {
    sortedDict[value] = [];
    sortedDict[value].push(key);
  } else {
    sortedDict[value].push(key);
  }
}
console.log(sortedDict);
