from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for i in range(N):
    emp = list(map(int, input().split()))
    lst.append(emp)

# 안전거리
def safe_dist(si, sj):
    global dist
    di = [0, 1, -1, 0, 1, 1, -1, -1]
    dj = [1, 0, 0, -1, 1, -1, 1, -1]

    q = deque()
    q.append([si, sj, 0])
    visited[si][sj] = True

    while q:
        ci, cj, cd = q.popleft()

        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if lst[ni][nj] == 1:
                    return cd + 1
                visited[ni][nj] = True
                q.append((ni, nj, cd + 1))

result = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            visited = [[False] * M for _ in range(N)] 
            dist = safe_dist(i, j)
            if dist is not None:
                result = max(result, dist)

print(result)