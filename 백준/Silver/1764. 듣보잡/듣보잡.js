const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = input[0].split(" ").map(Number)[0];
const M = input[0].split(" ").map(Number)[1];

let eme = new Set();
let emeqh = [];

for (let i = 1; i < N + M + 1; i++) {
  if (i <= N) {
    eme.add(input[i].trim());
  } else {
    let qh = input[i].trim();
    if (eme.has(qh)) {
      emeqh.push(qh);
    }
  }
}

emeqh.sort();
console.log(emeqh.length);
for (let gg of emeqh) {
  console.log(gg);
}
