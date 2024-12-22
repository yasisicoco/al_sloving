const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const array = input.map((item) => item.trim());
const N = parseInt(array[0]);
const pattern = array[1].split("*");

const patternStart = pattern[0];
const patternEnd = pattern[1];

for (let i = 2; i < N + 2; i++) {
  if (
    array[i].startsWith(patternStart) && // 맨앞 확인
    array[i].endsWith(patternEnd) && // 맨뒤 확인
    patternStart.length + patternEnd.length <= array[i].length // 길이 확인
  ) {
    console.log("DA");
  } else {
    console.log("NE");
  }
}
