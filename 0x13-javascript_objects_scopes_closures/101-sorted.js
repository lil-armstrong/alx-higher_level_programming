#!/usr/bin/node

const { dict } = require('./101-data');
const obj = {};
Object.entries(dict).forEach(([k, v]) => {
  if (v in obj) { obj[v].push(k); } else { obj[v] = [k]; }
});

console.log(obj);
