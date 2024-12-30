const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [N, M] = input[0].split(" ").map(Number);
let A = [];
let B = [];

for (let i = 1; i <= N; i++) {
  A.push(input[i].split(" ").map(Number));
}
for (let i = N + 1; i <= N * 2; i++) {
  B.push(input[i].split(" ").map(Number));
}

let mix = Array.from(Array(N), () => Array(M).fill(0));
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    mix[i][j] = A[i][j] + B[i][j];
  }
}

for (let k = 0; k < N; k++) {
  console.log(mix[k].join(" "));
}
