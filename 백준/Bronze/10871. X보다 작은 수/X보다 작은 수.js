const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const [N, X] = input[0].split(" ").map(Number);
const A = input[1].split(" ").map(Number);

let array = new Array();
for (let i = 0; i < N; i++) {
  if (A[i] < X) {
    array.push(A[i]);
  }
}
console.log(...array);
