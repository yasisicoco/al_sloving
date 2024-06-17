const fs = require("fs")
// let input = fs.readFileSync("./input.txt").toString().split(' ').map(Number)

let input = fs.readFileSync("/dev/stdin").toString().split(' ').map(Number)

const a = input[0]
const b = input[1]
console.log(a + b)