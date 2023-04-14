#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];

  let i = list.length - 1;
  for (;i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
