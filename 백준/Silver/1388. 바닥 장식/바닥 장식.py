import sys
sys.setrecursionlimit(10 ** 6)

di = [0, 1]
dj = [1, 0]

def dfs_garo(si, sj):
    global cnt
    if arr[si][sj] != '-':
        return
        
    ni = si + di[0]
    nj = sj + dj[0]
    if 0 <= ni < N and 0 <= nj < M and not vis[ni][nj] and arr[ni][nj] == '-':
        vis[ni][nj] = True
        dfs_garo(ni, nj)

def dfs_sero(si, sj):
    global cnt
    if arr[si][sj] != '|':
        return
    
    ni = si + di[1]
    nj = sj + dj[1]
    if 0 <= ni < N and 0 <= nj < M and not vis[ni][nj] and arr[ni][nj] == '|':
        vis[ni][nj] = True
        dfs_sero(ni, nj)
        
N, M = map(int, input().split())
arr = [input() for _ in range(N)]
vis = [[False] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '-' and not vis[i][j]:
            vis[i][j] = True
            dfs_garo(i, j)
            cnt += 1
        elif arr[i][j] == '|' and not vis[i][j]:
            vis[i][j] = True
            dfs_sero(i, j)
            cnt += 1
            
print(cnt)