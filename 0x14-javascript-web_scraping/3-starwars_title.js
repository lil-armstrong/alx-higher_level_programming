#!/usr/bin/node
const req = require('request');
const movieID = process.argv[2] || '';
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

req.get(endpoint, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const obj = JSON.parse(body);
  console.log(obj?.title);
});
