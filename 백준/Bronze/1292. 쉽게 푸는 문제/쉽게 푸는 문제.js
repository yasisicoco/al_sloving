const fs = require("fs");
const [A, B] = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);

const array = [];
for (let i = 0; i <= 1000; i++) {
  if (i <= 1000) {
    for (let j = 0; j < i; j++) {
      array.push(i);
    }
  }
}

let sum = 0;
for (let i = A - 1; i < B; i++) {
  sum += array[i];
}

console.log(sum);
