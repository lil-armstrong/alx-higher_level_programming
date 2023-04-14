#!/usr/bin/node
const { argv } = require('process');
const n = +argv[2];
if (n > 0) {
  if (Number.isNaN(n)) { console.log('Missing number of occurrences'); } else {
    for (let i = 0; i < n; i++) {
      console.log('C is fun');
    }
  }
}
