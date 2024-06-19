function dfs(friends, visited, cur, depth) {
  if (depth === 2) {
    return
  }

  for (let i of friends[cur]) {
    if (!visited[i]) {
      visited[i] = true
    }
    dfs(friends, visited, i, depth+1)
  }
}

const fs = require('fs')
// const input = fs.readFileSync('input.txt').toString().trim().split('\n')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const n = parseInt(input[0])
const m = parseInt(input[1])

let visited = new Array(n+1).fill(false)
visited[1] = true

let friends = Array.from({ length: n + 1 }, () => []);
for (let i = 2; i < 2+m; i++) {
  let [a, b] = input[i].trim().split(' ').map(Number)
  if (!friends[a]) friends[a] = [];
  if (!friends[b]) friends[b] = [];
  friends[a].push(b)
  friends[b].push(a)
}

dfs(friends, visited, 1, 0)
// console.log(friends)
// console.log(visited)
console.log(visited.filter(x=>x).length-1)