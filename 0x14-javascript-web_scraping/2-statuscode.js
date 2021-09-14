#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + res.statusCode);
});
