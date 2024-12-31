const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let winner = 0;
let winner_score = 0;
let sum = 0;

for (let i = 0; i < input.length; i++) {
  const chef_score = input[i]
    .split(" ")
    .map(Number)
    .reduce((acc, cur) => acc + cur, 0);
  if (sum < chef_score) {
    sum = chef_score;
    winner_score = chef_score;
    winner = i + 1;
  }
}
console.log(winner, winner_score);
