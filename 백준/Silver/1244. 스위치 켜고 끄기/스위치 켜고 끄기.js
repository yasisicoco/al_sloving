const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const array = input[1].split(" ").map(Number);
const stuNum = parseInt(input[2]);

for (let i = 3; i < stuNum + 3; i++) {
  const student = input[i].split(" ").map(Number);

  // 남학생1 = 스위치번호가 자기가 받은 수의 배수이면, 스위치의 상태바꿈
  if (student[0] === 1) {
    for (let j = 1; j * student[1] <= array.length; j++) {
      const boy = j * student[1] - 1;
      array[boy] = 1 - array[boy];
    }
  } else {
    // 여학생2 = 스위치번호를 중심으로 대칭되는 스위치가 다를때까지 바꿈
    const girl = student[1] - 1;
    array[girl] = 1 - array[girl];
    for (let k = 1; k < array.length; k++) {
      const girlPrev = girl - k;
      const girlNext = girl + k;
      if (
        array[girlPrev] === array[girlNext] &&
        girlPrev >= 0 &&
        girlNext < array.length
      ) {
        array[girlPrev] = 1 - array[girlPrev];
        array[girlNext] = 1 - array[girlNext];
      } else {
        break;
      }
    }
  }
}

for (let i = 0; i < array.length; i += 20) {
  console.log(array.slice(i, i + 20).join(" "));
}
