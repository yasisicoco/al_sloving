const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
let arr = input.slice(1, N + 1).map((item) => item.split(" ").map(Number));

// 1부터 N까지의 국가들의 index[1] index[2] index[3] 을 차례로 비교해서 sort
arr.sort((a, b) => {
  if (a[1] !== b[1]) {
    return b[1] - a[1];
  } else if (a[2] !== b[2]) {
    return b[2] - a[2];
  } else {
    return b[3] - a[3];
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

let target = arr.findIndex((country) => country[0] === K);
console.log(lst[target]);
