#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(number => parseInt(number));
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  let max2 = min;
  numbers.forEach(element => {
    if (element >= max2 && element < max) {
      max2 = element;
    }
    // console.log(typeof numbers[1])
  });
  console.log(max2);
}
