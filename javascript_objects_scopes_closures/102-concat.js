#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
const fileA = fs.readFileSync(args[0]);
const fileB = fs.readFileSync(args[1]);
const fileC = `${fileA}\n${fileB}`;
fs.writeFileSync('./fileC', args[2], (err) => {
  if (err) {
    console.log(err);
  }
});
