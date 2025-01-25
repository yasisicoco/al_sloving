const fs = require("fs");
const arr = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const lst = arr.reduce((acc, val) => acc + val, 0);
let a;
let b;
for (let i = 0; i < arr.length; i++) {
  for (let j = 1; j < arr.length; j++) {
    if (lst - (arr[i] + arr[j]) === 100) {
      a = arr[i];
      b = arr[j];
    }
  }
}

arr.sort((a, b) => a - b);
for (let k of arr) {
  if (k === a || k === b) continue;
  console.log(k);
}
