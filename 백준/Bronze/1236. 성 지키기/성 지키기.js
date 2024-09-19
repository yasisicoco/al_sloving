const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

let [N, M] = input[0].split(" ").map(Number);
let arr = Array();
for (let i = 1; i <= N; i++) {
  let row = input[i].trim();
  arr.push(row);
}

let rowCount = 0;
let colCount = 0;

for (let i = 0; i < N; i++) {
  if (arr[i].includes("X")) {
    rowCount += 1;
    continue;
  }
}

let empty = true;
for (let i = 0; i < M; i++) {
  empty = true;
  for (let j = 0; j < N; j++) {
    if (arr[j][i] === "X") {
      empty = false;
    }
  }
  if (empty === false) {
    continue;
  }
  colCount += 1;
}
// console.log(N - rowCount);
// console.log(colCount);
console.log(Math.max(N - rowCount, colCount));
