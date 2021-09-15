#!/usr/bin/node
const request = require('request');

const starwars = 'https://swapi-api.hbtn.io/api/films/';
request(starwars + process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);
  main(movie);
});

async function main (movie) {
  for (const charac of movie.characters) {
    const character = await doRequest(charac);
    console.log(character);
  }
}

function doRequest (charac) {
  return new Promise(function (resolve, reject) {
    request(charac, function (err, res, body) {
      if (!err) {
        resolve(JSON.parse(body).name);
      } else {
        reject(err);
      }
    });
  });
}
