#!/usr/bin/node
const { argv } = require('node:process');
const l = +argv[2];
const r = +argv[3];

function add (a, b) {
  return a + b;
}

console.log(add(l, r));
