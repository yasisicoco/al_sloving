const fs = require('fs');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);

let cnt = 0; // 좋은단어 수
for (let i=1; i <= N; i++) {
    let arr = input[i].trim();
    let st = new Array;
    
    for (let i=0; i < arr.length; i++) {
        if (st) {
            if (st[st.length-1] === arr[i]) {
                st.pop();
            } else {
                st.push(arr[i]);
            };
        } else {
            st.push(arr[i]);
        };
    };
    if (st.length === 0) {
        cnt += 1;
    };
};

console.log(cnt);