#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const [key, value] in Object.entries(dict)) {
  if (Object.hasOwn(newDict, value)) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
