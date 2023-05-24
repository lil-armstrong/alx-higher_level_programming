#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    const characters = responseJSON.characters;
    characters.forEach((link) => {
      request.get(link, (err, resp) => {
        if (err) {
          console.error(err);
          return;
        }

        if (resp.statusCode === 200) {
          const obj = JSON.parse(resp.body);
          console.log(obj?.name);
          return;
        }
        console.error(
					`Encountered an error with status code: ${resp.statusCode}`
        );
      });
    });
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
