const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const recom = parseInt(input[1]);
const arr = input[2].split(" ").map(Number);

// 2 6 7
let frame = {};
for (let i = 0; i < recom; i++) {
  if (arr[i] in frame) {
    frame[arr[i]][0]++;
  } else {
    if (Object.keys(frame).length < N) {
      frame[arr[i]] = [1, i]; // 추천수, 들어온 순서
    } else {
      let delFrame = Object.entries(frame).sort((a, b) => {
        if (a[1][0] !== b[1][0]) {
          return a[1][0] - b[1][0];
        }
        return a[1][1] - b[1][1];
      });
      delete frame[delFrame[0][0]];
      frame[arr[i]] = [1, i];
    }
  }
}
let result = Object.keys(frame).sort((a, b) => parseInt(a) - parseInt(b));
console.log(result.join(" "));
