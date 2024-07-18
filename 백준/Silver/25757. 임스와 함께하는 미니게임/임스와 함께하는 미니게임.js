const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [N, G] = input[0].trim().split(" ");
N = parseInt(N);

let person;
if (G === "Y") {
  person = 1;
} else if (G === "F") {
  person = 2;
} else if (G === "O") {
  person = 3;
}

let party = new Set();
for (let i = 1; i < N + 1; i++) {
  party.add(input[i].trim());
}
console.log(Math.floor(party.size / person));
