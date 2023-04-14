#!/usr/bin/node

exports.callMeMoby = function moby (x, cb) {
  for (let i = 0; i < x; i++) { cb(); }
};
