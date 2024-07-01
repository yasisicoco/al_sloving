const fs = require("fs");
// let input = fs.readFileSync("./input.txt").toString().trim().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 1. 만약 hp가 0이 되면 끝. 즉 99까지 쓸 수 있다.
// 2. 주어진 hp내에서 최대 happy 구하기

function back(cnt, h, hap) {
  if (h > 0) {
    maxHappy = Math.max(maxHappy, hap);
  }
  
  if (cnt === N) {
    return
  }
  
  back(cnt+1, h-lose[cnt], hap+get[cnt]);
  back(cnt+1, h, hap);
};

const N = parseInt(input[0]);
const lose = input[1].split(' ').map(Number);
const get = input[2].split(' ').map(Number);

let hp = 100;
let maxHappy = 0;

back(0, hp, 0);
console.log(maxHappy);