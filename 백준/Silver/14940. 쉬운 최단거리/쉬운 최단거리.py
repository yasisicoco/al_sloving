import sys
from collections import deque
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(si, sj):
    visited[si][sj] = True
    q = deque()
    q.append([si, sj])
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 0:
                visited[ni][nj] = True
                cnt[ni][nj] = cnt[ci][cj] + 1
                q.append([ni, nj])
        

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j) # 갈 수 있는 땅 체크
            
for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1:
            cnt[i][j] = -1
for line in cnt:
    print(*line)