const fs = require("fs")
// let input = fs.readFileSync("./input.txt").toString().trim().split(' ')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(' ')

const a = parseInt(input[0], 10)
const b = parseInt(input[1], 10)

if (a > b) {
  console.log(">")
} else if (a < b) {
  console.log("<")
} else if (a === b) {
  console.log("==")
}