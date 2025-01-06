const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();

let num = Number(input);
const first_num = num;
let cnt = 0;

while (true) {
  let a = num % 10;
  let b = Math.floor(num / 10);
  num = a * 10 + ((a + b) % 10);
  cnt += 1;
  if (num === first_num) break;
}

console.log(cnt);
