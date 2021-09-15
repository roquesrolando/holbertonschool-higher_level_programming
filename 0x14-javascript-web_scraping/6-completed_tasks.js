#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todo = JSON.parse(body);
  let dict = {};
  let user = 1;
  let count = 0;
  for (const task of todo) {
    if (task.userId !== user) {
      user++;
      count = 0;
    }
    if (task.completed) {
      count++;
      dict[task.userId] = count;
    }
  }
  console.log(dict);
});
