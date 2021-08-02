#!/usr/bin/node

const number = process.argv.slice(2).map(Number);
let second = 0;

if (number.length > 1) {
  second = number.sort((a, b) => (b - a))[1];
}
console.log(second);
