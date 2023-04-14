#!/usr/bin/node
function cb () {
  let nargs = 0;

  return (item) => {
    console.log(`${nargs}: ${item}`);
    nargs++;
  };
}
exports.logMe = cb();
