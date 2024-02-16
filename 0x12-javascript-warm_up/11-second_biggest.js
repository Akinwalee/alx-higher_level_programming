#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  let max = Number.NEGATIVE_INFINITY;
  let max2 = Number.NEGATIVE_INFINITY;
  for (let i = 0; i < args.length; i++) {
    if (Number(args[i]) > max) {
      max2 = max;
      max = Number(args[i]);
    }
    if (Number(args[i]) > max2 && Number(args[i]) !== max) {
      max2 = Number(args[i]);
    }
  }
  console.log(max2);
}
