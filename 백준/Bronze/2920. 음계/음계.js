const fs = require("fs");
const array = fs.readFileSync("/dev/stdin").toString().split(" ").map(Number);

const ascending = [1, 2, 3, 4, 5, 6, 7, 8];
const descending = [8, 7, 6, 5, 4, 3, 2, 1];

let ascending_flag = true;
let descending_flag = true;
for (let i = 0; i < array.length; i++) {
  if (array[i] !== ascending[i]) {
    ascending_flag = false;
  }
  if (array[i] !== descending[i]) {
    descending_flag = false;
  }
}
if (ascending_flag === true) {
  console.log("ascending");
} else if (descending_flag === true) {
  console.log("descending");
} else console.log("mixed");
