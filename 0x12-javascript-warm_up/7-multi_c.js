#!/usr/bin/node
const { argv } = require('process');
const n = +argv[2];

if (Number.isNaN(n) || n <= 0) { console.log('Missing number of occurrences'); } else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
