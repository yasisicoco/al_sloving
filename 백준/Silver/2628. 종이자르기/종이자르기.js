const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const slice = Number(input[1]);

const row_arr = [0, N];
const col_arr = [0, M];

for (let i = 0; i < slice; i++) {
  // 0 : 세로선 , 1 : 가로선
  const [j, k] = input[i + 2].split(" ").map(Number);
  if (j === 0) {
    col_arr.push(k);
  } else if (j === 1) {
    row_arr.push(k);
  }
}

row_arr.sort((a, b) => a - b);
col_arr.sort((a, b) => a - b);
let row_max = 0;
let col_max = 0;
for (let i = 0; i < row_arr.length; i++) {
  if (i + 1 < row_arr.length) {
    const row_val = row_arr[i + 1] - row_arr[i];
    row_max = Math.max(row_val, row_max);
  }
}
for (let i = 0; i < col_arr.length; i++) {
  if (i + 1 < col_arr.length) {
    const col_val = col_arr[i + 1] - col_arr[i];
    col_max = Math.max(col_val, col_max);
  }
}
console.log(row_max * col_max);
