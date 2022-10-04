#!/usr/bin/node
const args = process.argv.slice(2);
if (Number(args[0]) == args[0]) {
  console.log('My number: ' + Number(args[0]));
} else {
  console.log('Not a number');
}
