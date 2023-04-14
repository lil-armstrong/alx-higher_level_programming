#!/usr/bin/node
const { argv } = require('process');
const n = +argv[2];

if (Number.isNaN(n) || n <= 0) { console.error('Missing size'); } else {
  for (let i = 0; i < n; ++i) {
    let row = '';
    for (let j = 0; j < n; ++j) {
      row += 'X';
    }
    console.log(row);
  }
}
