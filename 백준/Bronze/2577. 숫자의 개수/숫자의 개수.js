const fs = require("fs");
const [A, B, C] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map(Number);

const num = A * B * C;
const num_str = num.toString();
let array = new Array(10).fill(0);
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < num_str.length; j++) {
    const str = Number(num_str[j]);
    if (str === i) {
      array[i] += 1;
    }
  }
}

array.forEach((item) => console.log(item));
