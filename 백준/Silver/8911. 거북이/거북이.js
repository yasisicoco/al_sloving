const fs = require("fs");
// let input = fs.readFileSync("./input.txt").toString().trim().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const di = [-1, 0, 1, 0]
const dj = [0, 1, 0, -1]
let dir = 0
const T = parseInt(input[0])

for (let i=1; i <= T; i++) {
  let commend = input[i]
  let start = new Array(2).fill(0)
  let min_x = 0, max_x = 0, min_y = 0, max_y = 0;

  for (let c of commend) {
    if (c === 'F') {
      start[0] += di[dir]
      start[1] += dj[dir]
      } else if (c === 'B') {
        start[0] -= di[dir]
        start[1] -= dj[dir]  
    } else if (c === 'L') {
      dir = (dir - 1 + 4) % 4
    } else if (c === 'R') {
      dir = (dir + 1) % 4
    }

    min_x = Math.min(min_x, start[0])
    max_x = Math.max(max_x, start[0])
    min_y = Math.min(min_y, start[1])
    max_y = Math.max(max_y, start[1])
  }

  console.log(Math.abs(max_x - min_x) * Math.abs(max_y - min_y))
}