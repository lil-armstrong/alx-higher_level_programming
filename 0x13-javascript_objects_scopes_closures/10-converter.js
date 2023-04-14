#!/usr/bin/node

exports.converter = (base) => {
  return (n) => Number(n).toString(base);
};
