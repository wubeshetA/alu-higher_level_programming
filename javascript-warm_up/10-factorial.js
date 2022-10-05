#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (n) {
  if (n < 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const n = parseInt(args[0]);
if (isNaN(n)) {
  console.log(1);
} else console.log(factorial(n));
