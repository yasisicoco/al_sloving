const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");
// const input = fs.readFileSync("./input.txt").toString().trim();

const N = parseInt(input[0]);
let result;

for (let i = 1; i <= 9; i++) {
  result = N * i;
  console.log(N, "*", i, "=", result);
}
