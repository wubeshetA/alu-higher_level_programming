#!/usr/bin/node
const args = process.argv.slice(2);
// check if the first argument can be converted to a number.
if (isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
