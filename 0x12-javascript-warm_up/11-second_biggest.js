#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  let max = Number(args[2]);
  let max2 = Number(args[2]);
  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      max2 = max;
      max = args[i];
    }
  }
  console.log(max2);
}
