const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
let ans = input[1].trim();

for (let i = 2; i < N + 1; i++) {
  let cnt = 0;
  let result = "";

  while (cnt < ans.length) {
    let anx = input[i];
    if (ans[cnt] === anx[cnt]) {
      result += anx[cnt];
    } else {
      result += "?";
    }
    cnt += 1;
  }
  ans = result;
}
console.log(ans);
