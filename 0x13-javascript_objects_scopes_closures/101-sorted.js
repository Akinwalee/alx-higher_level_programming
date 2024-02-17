#!/usr/bin/node

const dict = require('101-data').dict;

for (let key in dict) {
  const value = dict[key];
  dict[key] = key;
  key = value;
}

console.log(dict);
