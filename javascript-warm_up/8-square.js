#!/usr/bin/node
const args = process.argv.slice(2);
// check if the first argument can be converted to a number.
if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(parseInt(args[0]));
  for (let i = 0; i < args[0]; i++) {
    console.log(row);
  }
}
