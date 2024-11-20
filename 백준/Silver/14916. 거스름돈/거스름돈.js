const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// const input = fs.readFileSync("./input.txt").toString().trim().split("\n");

// 5로 나누어서 나누어떨어지는 경우 = 5원으로 먼저 계산
// 5로 나누어지지 않을 때, 맨 뒷자리가 3,8인경우 2원 4개
// 5로 나누어지지 않을 때, 맨 뒷자리가 1,6인경우 2원 3개
// 5원보다 아래일 때, 1, 3원인 경우 -1 출력

let n = parseInt(input[0]);

function Coins(amount) {
  if ((amount < 5 && amount == 1) || (amount < 5 && amount == 3)) {
    return -1;
  }

  let count = 0;

  if (amount % 5 === 0) {
    count = amount / 5;
  } else {
    while (amount > 0) {
      if (amount % 5 === 0) {
        count += amount / 5;
        break;
      } else if (amount % 10 === 3 || amount % 10 === 8) {
        count += 4;
        amount -= 8;
      } else if (amount % 10 === 1 || amount % 10 === 6) {
        count += 3;
        amount -= 6;
      } else if (amount === 1 || amount === 3) {
        return -1;
      } else {
        count++;
        amount -= 2;
      }
    }
  }

  return count;
}

console.log(Coins(n));
