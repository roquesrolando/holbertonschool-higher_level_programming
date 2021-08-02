#!/usr/bin/node

function factorial (n) {
  if (n <= 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
const number = parseInt(process.argv[2]);
if (number) {
  console.log(factorial(number));
} else {
  console.log('1');
}
