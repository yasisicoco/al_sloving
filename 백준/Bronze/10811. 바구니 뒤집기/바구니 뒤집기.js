const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ");
let basket = Array.from({ length: N }, (_, index) => index + 1);

for (let i = 1; i <= M; i++) {
  const [s, e] = input[i].split(" ");

  let ref = basket.slice(s - 1, e);
  ref.reverse();
  basket.splice(s - 1, e - s + 1, ...ref);
}

console.log(basket.join(" "));
