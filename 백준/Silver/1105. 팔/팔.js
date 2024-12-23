const fs = require("fs");

// 파일에서 입력을 읽어오기
const [A, B] = fs.readFileSync("./dev/stdin").toString().trim().split(" ");

// 결과를 저장할 변수
let ret = 0;

// A와 B의 길이가 다르면 0을 출력
if (A.length !== B.length) {
  console.log(0);
} else {
  // 길이가 같을 때, 각 자리를 비교
  for (let i = 0; i < A.length; i++) {
    if (A[i] === B[i]) {
      if (A[i] === "8") {
        ret++;
      }
    } else {
      break;
    }
  }
  // 최종 결과 출력
  console.log(ret);
}
