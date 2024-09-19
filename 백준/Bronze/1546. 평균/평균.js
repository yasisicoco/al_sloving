const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const N = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);
const M = Math.max(...arr);
// console.log(M);
let newScore;
let result = 0;
for (let i of arr) {
  newScore = (i / M) * 100;
  result += newScore;
}

console.log((result / N).toFixed(2));
