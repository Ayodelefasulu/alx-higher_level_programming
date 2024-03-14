#!/usr/bin/node

let n = 0;

exports.logMe = function (item) {
  if (item) {
    console.log(`${n} : ${item}`);
  }
  n++;
};
