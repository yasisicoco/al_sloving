const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

let arr = input[0];
let result = 0;

for (let i = 0; i < arr.length; i++) {
  if (arr[i] === "c" && (arr[i + 1] === "=" || arr[i + 1] === "-")) {
    result++;
    i++; // 다음 문자로 건너뜀
  } else if (arr[i] === "d" && arr[i + 1] === "z" && arr[i + 2] === "=") {
    result++;
    i += 2; // 다음 두 문자로 건너뜀
  } else if (arr[i] === "d" && arr[i + 1] === "-") {
    result++;
    i++; // 다음 문자로 건너뜀
  } else if ((arr[i] === "l" || arr[i] === "n") && arr[i + 1] === "j") {
    result++;
    i++; // 다음 문자로 건너뜀
  } else if ((arr[i] === "s" || arr[i] === "z") && arr[i + 1] === "=") {
    result++;
    i++; // 다음 문자로 건너뜀
  } else {
    result++; // 조건에 해당하지 않으면 그냥 1을 더함
  }
}

console.log(result);
