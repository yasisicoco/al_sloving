const fs = require("fs");
// let input = fs.readFileSync("./input.txt").toString().trim().split(" ");
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
let H = parseInt(input[0], 10);
let M = parseInt(input[1], 10);

if (0 <= H && H <= 23 && 0 <= M && M <= 59) {
  if (M < 45) {
    H = H - 1;
    M = M + 15;
    if (H < 0) {
      H = H + 24;
    }
  } else {
    M = M - 45;
  }
  console.log(H, M);
}
