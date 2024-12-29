const fs = require("fs");
let [hour, minute] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(Number);

if (0 <= hour <= 23 && 0 <= minute <= 59) {
  if (minute < 45) {
    hour -= 1;
    minute += 15;
    if (hour < 0) {
      hour += 24;
    }
  } else {
    minute -= 45;
  }
}
{
  console.log(hour, minute);
}
