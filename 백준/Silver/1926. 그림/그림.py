import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def dfs(si, sj):
    global size_comp
    
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        
        if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj] and arr[ni][nj] == 1:
            vis[ni][nj] = True
            size_comp += 1
            dfs(ni, nj)
            
    
# 세로 | 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]

cnt = 0
size = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not vis[i][j]:
            size_comp = 1
            vis[i][j] = True
            dfs(i, j)
            cnt += 1
            size = max(size_comp, size)
        
print(cnt)
print(size)