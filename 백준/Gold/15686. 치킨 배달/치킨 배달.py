import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(cnt, k):
    global result
    val = 0
    
    if cnt == M:
        for r in house:
            rr, rc = r[0], r[1]
            dist = 2*N
            
            for c in select:
                cr, cc = c[0], c[1]
                tmp = abs(rr-cr) + abs(rc-cc)
                if tmp < dist:
                    dist = tmp
            val += dist
        
        if val < result:
            result = min(val, result)
            return
    
    for idx in range(k, K):
        select.append(chicken[idx])
        dfs(cnt+1, idx+1)
        select.pop()

chicken = deque()
house = deque()

select = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

K = len(chicken)
result = 10e9

for k in range(K):
    dfs(0, k)
    
print(result)