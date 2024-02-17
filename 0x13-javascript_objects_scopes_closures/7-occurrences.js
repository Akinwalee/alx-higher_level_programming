#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const item in list) {
    if (item === searchElement) {
      count += 1;
    }
  }

  return (count);
};
