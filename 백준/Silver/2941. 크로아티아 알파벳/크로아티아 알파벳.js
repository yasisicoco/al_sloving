const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");


let arr = input[0];
let result = 0;

for (let i = 0; i < arr.length; i++) {
  result++;
  if (arr[i] === "c" && (arr[i + 1] === "=" || arr[i + 1] === "-")) {
    i++;
  } else if (arr[i] === "d" && arr[i + 1] === "z" && arr[i + 2] === "=") {
    i += 2;
  } else if (arr[i] === "d" && arr[i + 1] === "-") {
    i++;
  } else if ((arr[i] === "l" || arr[i] === "n") && arr[i + 1] === "j") {
    i++;
  } else if ((arr[i] === "s" || arr[i] === "z") && arr[i + 1] === "=") {
    i++;
  }
}
console.log(result);
