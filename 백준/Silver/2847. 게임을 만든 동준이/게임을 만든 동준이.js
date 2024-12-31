const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number);

// 뒤에서부터 읽는 배열
const N = input[0];
const level = input.slice(1).map(Number);
let count = 0;

for (let i = N - 1; i > 0; i--) {
  while (level[i - 1] >= level[i]) {
    level[i - 1] -= 1;
    count += 1;
  }
}
console.log(count);
