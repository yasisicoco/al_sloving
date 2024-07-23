const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let N = parseInt(input[0].trim(), 10);
for (let i = 1; i < N + 1; i++) {
  let arr = input[i];
  let st = 0;
  let ans = 0;
  for (let j = 0; j < arr.length; j++) {
    if (arr[j] === "O") {
      st += 1;
      ans += st;
    } else if (arr[j] === "X") {
      st = 0;
    }
  }
  console.log(ans);
}
