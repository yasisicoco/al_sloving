const fs = require("fs")
// let input = fs.readFileSync("./input.txt").toString().trim()
let input = fs.readFileSync("/dev/stdin").toString().trim()
const a = parseInt(input, 10)

if (a >= 90) {
  console.log("A")
} else if (a >= 80) {
  console.log("B")
} else if (a >= 70) {
  console.log("C")
} else if (a >= 60) {
  console.log("D")
} else {
  console.log("F")
}