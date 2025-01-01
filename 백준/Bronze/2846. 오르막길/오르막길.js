const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = input[0];
const array = input[1].split(" ").map(Number);

let sum_count = 0;
let count = 0;
for (let i = 0; i < N - 1; i++) {
  if (array[i] < array[i + 1]) {
    count += array[i + 1] - array[i];
  } else if (array[i] >= array[i + 1]) {
    count = 0;
  }
  sum_count = Math.max(count, sum_count);
}

console.log(sum_count);
