const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number);

let sum = 0;
let result = 0;

let under = 0;
let over = 0;
for (let i = 0; i < input.length; i++) {
  if (sum <= 100) {
    // 100보다 작으면 저장 후 더하기
    under = sum;
    sum += input[i];
  } else if (sum >= 100) {
    // 100보다 크면 under over 비교 후 100에 더 가까우면서 큰것 result 저장
    over = sum;
    if (Math.abs(100 - under) >= Math.abs(100 - over)) {
      result = over;
    } else {
      result = under;
    }
    console.log(result);
    break;
  }
}

if (sum < 100) {
  console.log(sum);
}
