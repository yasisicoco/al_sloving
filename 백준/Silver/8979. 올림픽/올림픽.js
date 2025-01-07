const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
let arr = input.slice(1, N + 1);

// 1부터 N까지의 국가들의 index[1] index[2] index[3] 을 차례로 비교해서 sort
arr = arr.sort((a, b) => {
  const aValues = a.split(" ").map(Number);
  const bValues = b.split(" ").map(Number);

  if (aValues[1] !== bValues[1]) {
    return bValues[1] - aValues[1];
  } else if (aValues[2] !== bValues[2]) {
    return bValues[2] - aValues[2];
  } else {
    return bValues[3] - aValues[3];
  }
});

function count(lst, target) {
  return lst.filter((item) => item === target).length;
}

let lst = [];
cnt = 1;
for (let i = 0; i < N - 1; i++) {
  if (
    arr[i][1] === arr[i + 1][1] &&
    arr[i][2] === arr[i + 1][2] &&
    arr[i][3] === arr[i + 1][3]
  ) {
    lst.push(cnt);
  } else {
    lst.push(cnt);
    cnt += count(lst, cnt);
  }
}
lst.push(cnt);

for (let j = 0; j < N; j++) {
  if (j === K) {
    console.log(lst[j]);
  }
}
