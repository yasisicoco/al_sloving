const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

function D(n) {
    n = n * 2;
    if (n >= 10000) {
        n = n % 10000;
    }
    return n;
}

function S(n) {
    n = n - 1;
    if (n === -1) {
        n = 9999;
    }
    return n;
}

function L(n) {
    return (n % 1000) * 10 + Math.floor(n / 1000);
}

function R(n) {
    return (n % 10) * 1000 + Math.floor(n / 10);
}

function bfs(a, b) {
    const q = [];
    q.push([a, '']);
    const visited = new Array(10000).fill(0);
    visited[a] = 1;

    while (q.length > 0) {
        const [nn, ss] = q.shift();
        for (const [operation, op_name] of [[D, 'D'], [S, 'S'], [L, 'L'], [R, 'R']]) {
            const result = operation(nn);
            if (result === b) {
                console.log(ss + op_name);
                return;
            }

            if (visited[result] === 0) {
                visited[result] = 1;
                q.push([result, ss + op_name]);
            }
        }
    }
}

const T = parseInt(input[0]);
for (let i = 1; i <= T; i++) {
    const [A, B] = input[i].split(' ').map(Number);
    bfs(A, B);
}
