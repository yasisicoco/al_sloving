const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const K = Number(input[0]);

const directions = input.slice(1).map((line) => line.split(" ").map(Number));

let maxWidth = 0,
  maxHeight = 0;
let widthIndex = -1,
  heightIndex = -1;

// 1. 가장 긴 가로와 세로 변 찾기
// 2. 가장 긴 가로와 세로의 양옆을 빼서 작은사각형의 변 구하기
for (let i = 0; i < 6; i++) {
  const [direction, length] = directions[i];
  if (direction === 1 || direction === 2) {
    //동서
    if (length > maxWidth) {
      maxWidth = length;
      widthIndex = i;
    }
  } else {
    //남북
    if (length > maxHeight) {
      maxHeight = length;
      heightIndex = i;
    }
  }
}

const smallWidth = Math.abs(
  directions[(widthIndex + 5) % 6][1] - directions[(widthIndex + 1) % 6][1]
);
const smallHeight = Math.abs(
  directions[(heightIndex + 5) % 6][1] - directions[(heightIndex + 1) % 6][1]
);

const result = (maxWidth * maxHeight - smallWidth * smallHeight) * K;
console.log(result);
