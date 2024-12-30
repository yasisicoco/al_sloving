const fs = require("fs");
const [A, B, C] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map(Number);

const num = (A * B * C).toString();
let array = new Array(10).fill(0);
for (let count of num) {
  array[Number(count)]++;
}

console.log(array.join("\n"));
