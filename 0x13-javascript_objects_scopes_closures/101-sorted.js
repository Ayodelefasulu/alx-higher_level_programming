#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable no-unused-vars */

const dict = require('./101-data').dict;

const sortedDict = {};

for (const key in dict) {
  const value = dict[key];
  if (!(value in sortedDict)) {
    sortedDict[value] = [];
  }
  sortedDict[value].push(key);
}

console.log(sortedDict);
