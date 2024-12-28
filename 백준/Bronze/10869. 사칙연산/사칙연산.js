const fs = require("fs");
const [A, B] = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);

console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(Math.floor(A / B));
console.log(A % B);
