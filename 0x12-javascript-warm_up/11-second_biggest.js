#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
if (!args.length || args.length === 1) { console.log(0); } else {
  const sorted = args.sort();
  console.log(sorted);
  console.log(sorted[sorted.length - 2]);
}
