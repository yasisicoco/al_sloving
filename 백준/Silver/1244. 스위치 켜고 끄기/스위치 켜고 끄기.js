const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const array = input[1].split(" ").map(Number);
const stuNum = parseInt(input[2]);

for (let i = 3; i < stuNum + 3; i++) {
  const student = input[i].split(" ").map(Number);

  // 남학생1 = 스위치번호가 자기가 받은 수의 배수이면, 스위치의 상태바꿈
  if (student[0] === 1) {
    for (let j = 0; j < 101; j++) {
      const boy = student[1] * j - 1;
      if (array[boy] === 1 && boy < array.length) {
        array[boy] = 0;
      } else if (array[boy] === 0 && boy <= array.length) {
        array[boy] = 1;
      }
    }
  } else {
    // 여학생2 = 스위치번호를 중심으로 대칭되는 스위치가 다를때까지 바꿈
    const girl = student[1] - 1;
    if (array[girl] === 0) {
      array[girl] = 1;
    } else {
      array[girl] = 0;
    }
    for (let k = 1; k < 101; k++) {
      const girlPrev = girl - k;
      const girlNext = girl + k;
      if (
        array[girlPrev] === array[girlNext] &&
        girlPrev >= 0 &&
        girlNext <= 100
      ) {
        if (array[girlPrev] === 1) {
          array[girlPrev] = 0;
          array[girlNext] = 0;
        } else {
          array[girlPrev] = 1;
          array[girlNext] = 1;
        }
      } else {
        break;
      }
    }
  }
}

for (let i = 0; i < array.length; i += 20) {
  console.log(array.slice(i, i + 20).join(" "));
}
