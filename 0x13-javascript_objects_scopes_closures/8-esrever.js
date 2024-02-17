#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;

  for (let i = 0; i < len; i++) {
    const temp = list[i];
    list[i] = list[len - i];
    list[len - i] = temp;
  }
  return (list);
};
