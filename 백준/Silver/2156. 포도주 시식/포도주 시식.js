const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input[0].trim());
const arr = input.slice(1, n + 1).map(Number);
const dp = new Array(n).fill(0);

dp[0] = arr[0];
if (n > 1) dp[1] = arr[0] + arr[1];
if (n > 2) dp[2] = Math.max(arr[0] + arr[2], arr[1] + arr[2], dp[1]);

for (let i=3; i < n; i++) {
  dp[i] = Math.max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])
}
console.log(Math.max(...dp))