const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const arr = input[1].split(" ");

const M = Math.max(...arr.map(Number));
let NewScore = 0;
for (let i = 0; i < N; i++) {
  NewScore += (arr[i] / M) * 100;
}
console.log(NewScore / arr.length);
