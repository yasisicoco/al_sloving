const fs = require("fs");
const input = fs.readFileSync("./dev/stdin").toString().split("\n");

const N = parseInt(input[0]);
let arr = [];
for (let i = 1; i <= N; i++) {  // N+1 대신 <= N 사용
  arr.push(parseInt(input[i]));
}

// 숫자를 오름차순으로 정렬
const sortArr = arr.sort((a, b) => a - b);

for (let i = 0; i < N; i++) {
  console.log(sortArr[i]);
}
