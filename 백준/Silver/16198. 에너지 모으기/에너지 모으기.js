const fs = require("fs");
// let input = fs.readFileSync("./input.txt").toString().trim().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0])
const energy = input[1].split(' ').map(Number)

let ans = 0

function charge(energy, cur) {
  if (energy.length === 2) {
    ans = Math.max(ans, cur)
    return
  }

  for (let i = 1; i < energy.length - 1; i++) {
    let sumone = energy[i - 1] * energy[i + 1]
    let new_val = energy.splice(i, 1)[0]
    charge(energy, cur + sumone)
    energy.splice(i, 0, new_val)
  }
}

charge(energy, 0)
console.log(ans)