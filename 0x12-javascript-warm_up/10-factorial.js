#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = +argv[2];
function factorial (n) {
  if (Number.isNaN(n) || n <= 1) { return 1; }
  return n * factorial(n - 1);
}

console.log(factorial(arg1));
