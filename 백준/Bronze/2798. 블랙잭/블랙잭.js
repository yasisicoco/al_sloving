const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

// 확인해야할 길이가 N
// 만약 M보다 크면 패스 (M과 같거나 작은 값)
// 만약 M보다 작거나 같으면 result에 저장하고 이전 값으로 빼기

let result = 0;
let sum = 0;
for (let i = 0; i < N - 2; i++) {
  sum += arr[i];

  for (let j = i + 1; j < N - 1; j++) {
    sum += arr[j];

    for (let k = j + 1; k < N; k++) {
      sum += arr[k];
      if (sum <= M) {
        // 작은것중 최대값
        result = Math.max(sum, result);
      }
      sum -= arr[k];
    }

    sum -= arr[j];
  }

  sum -= arr[i];
}

console.log(result);
