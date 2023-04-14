#!/usr/bin/node
const { argv } = require('process');
const args = argv.slice(2);
if (args.length <= 0 || args.length === 1) { console.log(0); } else {
  const sorted = args.sort((a, b) => Number(a) > Number(b) ? 1 : -1 );
  console.log(sorted[sorted.length - 2]);
}
