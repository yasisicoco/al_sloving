const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number);

let students = Array.from({ length: 30 }, (_, index) => index + 1);
const findStudent = students.filter((student) => !input.includes(student));

console.log(findStudent.join("\n"));
