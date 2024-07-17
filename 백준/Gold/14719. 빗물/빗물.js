const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [H, W] = input[0].split(" ").map(Number);
const block = input[1].split(" ").map(Number);
let ans = 0;

for (let i = 0; i < W - 1; i++) {
  let left = Math.max(...block.slice(0, i));
  let right = Math.max(...block.slice(i + 1));
  let m = Math.min(left, right);
  if (m > block[i]) {
    ans += m - block[i];
  }
}

console.log(ans);
