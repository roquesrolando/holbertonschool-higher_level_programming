#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf8', err => {
    if (err) {
      console.error(err);
    }
  });
});
