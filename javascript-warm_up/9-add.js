#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  console.log(a + b);
}
add(Number(args[0]), Number(args[1]));
