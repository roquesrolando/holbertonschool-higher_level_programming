#!/usr/bin/node
const request = require('request');

const starwars = 'https://swapi-api.hbtn.io/api/films/';
request(starwars + process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);
  for (const charac of movie.characters) {
    request(charac, (err, res, body) => {
      if (err) {
        console.error(err);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
