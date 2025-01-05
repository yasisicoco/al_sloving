const fs = require("fs");
const input = fs.readFileSync("./dev/stdin").toString().trim().split(" ");

const A = input[0];
const B = input[1];
const N = A.length;
const M = B.length;

let same = "";
for (let k of A) {
  if (B.includes(k)) {
    same = k;
    break;
  }
}

let cntA = -1;
for (let j of A) {
  cntA++;
  if (same === j) {
    break;
  }
}

let cntB = -1;
for (let l of B) {
  cntB++;
  if (same === l) {
    break;
  }
}

let arr = Array.from({ length: M }, () => Array(N).fill("."));

for (let z = 0; z < M; z++) {
  arr[z][cntA] = B[z];
}
for (let x = 0; x < N; x++) {
  arr[cntB][x] = A[x];
}

console.log(arr.map((line) => line.join("")).join("\n"));
