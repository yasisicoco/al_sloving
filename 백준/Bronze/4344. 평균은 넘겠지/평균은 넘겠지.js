const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const C = Number(input[0]);
for (let i = 1; i <= C; i++) {
  // 배열
  const array = input[i].split(" ").map(Number);

  // 배열[i]의 평균
  const average = array.slice(1).reduce((acc, cur) => acc + cur, 0) / array[0];

  let count = 0;
  for (let j = 1; j <= array[0]; j++) {
    if (average < array[j]) {
      count += 1;
    }
  }

  let result = (count / array[0]) * 100;
  console.log(`${result.toFixed(3)}%`);
}
