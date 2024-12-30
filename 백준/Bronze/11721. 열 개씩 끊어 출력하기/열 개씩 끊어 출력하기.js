const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

let sentence = "";
let results = [];
for (let i = 0; i < input.length; i++) {
  if (sentence.length === 10) {
    results.push(sentence);
    sentence = input[i];
  } else {
    sentence += input[i];
  }
}
results.push(sentence);
for (let j = 0; j < results.length; j++) {
  console.log(results[j]);
}
