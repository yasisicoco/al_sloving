import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    cnt = 1
    q = deque()
    q.append([si, sj])
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == False:
                visited[ni][nj] = True
                cnt += 1
                q.append([ni, nj])
    return cnt # 영역 사이즈 들고나가기


M, N, K = map(int, input().split())
# 큰 그래프부터
arr = [[0] * N for _ in range(M)]

# 직사각형 그려주기
visited = [[False] * N for _ in range(M)] # 가지치기
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            if visited[i][j]:
                continue
            visited[i][j] = True
            arr[i][j] = 1  

# pprint(arr) # 그래프 최신화 확인
# 그래프를 전체 돌아주면서 각 영역의 사이즈 확인
site = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            size = bfs(i, j)
            site.append(size)

site.sort()
print(len(site))
print(*site)