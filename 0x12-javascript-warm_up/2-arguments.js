#!/usr/bin/node

const args = process.argv[2];

if (args == null) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
