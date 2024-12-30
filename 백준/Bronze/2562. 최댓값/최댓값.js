const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number);

let max_val = 0;
let count = 0;

for (let i = 0; i < input.length; i++) {
  if (max_val < input[i]) {
    max_val = input[i];
    count = i + 1;
  }
}

console.log(max_val);
console.log(count);
