#!/usr/bin/node

const arg = process.argv;
const arr = ['fun', 'cool', 'amazing'];

for (let i = 2; i < 5; i++) {
  console.log(`${arg[i]} is ${arr[i - 2]}`);
}
