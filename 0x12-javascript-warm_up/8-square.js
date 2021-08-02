#!/usr/bin/node

const count = parseInt(process.argv[2]);

if (count) {
  for (let i = 1; i <= count; i++) {
    for (let j = 2; j <= count; j++) {
      process.stdout.write('X');
    }
    console.log('X');
  }
} else {
  console.log('Missing size');
}
