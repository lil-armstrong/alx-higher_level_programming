#!/usr/bin/node
const req = require('request');
const movieID = process.argv[2] || '';
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

req.get(endpoint, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode != 200) {
    console.error(`Error code ${response.statusCode}`);
  }

  const obj = JSON.parse(body);
  console.log(obj?.title);
});
