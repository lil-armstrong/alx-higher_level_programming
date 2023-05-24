#!/usr/bin/node
const req = require('request');

const url = process.argv[2];

req.get(url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  const obj = JSON.parse(response?.body);
  const result = {};

  obj.forEach((rec) => {
    if (rec.completed) {
      if (rec.userId in result) {
        result[rec.userId]++;
      } else {
        result[rec.userId] = 1;
      }
    }
  });

  console.log(result);
});
