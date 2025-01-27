const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let line = 1;
const T = Number(input[0]);
for (let i = 0; i < T; i++) {
  const [E, TO] = input[line++].trim().split(" ").map(Number);
  let user = [];
  let time = [];
  let maxUser = 0;
  const allUser = new Set();

  for (let j = 0; j < E; j++) {
    const log = input[line++].trim().split(" ");
    const [hours, minutes] = log[0].split(":").map(Number);
    const newTime = hours * 60 + minutes;

    while (time.length && time[0] + TO <= newTime) {
      user.shift();
      time.shift();
    }

    if (log[1] === "USER") {
      if (log[3] === "LOG_IN") {
        user.push(log[2]);
        time.push(newTime);
        allUser.add(log[2]);
      } else {
        const idx = user.indexOf(log[2]);
        if (idx !== -1) {
          user.splice(idx, 1);
          time.splice(idx, 1);
        }
      }
    } else {
      user = [];
      time = [];
    }

    maxUser = Math.max(user.length, maxUser);
  }

  console.log(allUser.size, maxUser);
}
