# 적록색약이 아닌사람 / 적록색약인 사람
from collections import deque
import sys
input = sys.stdin.readline
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def colorcheck(si, sj):
    global color
    visited[si][sj] = True
    q = deque()
    q.append([si, sj])
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append([ni, nj])

def rgcheck(si, sj):
    global color
    rg_visited[si][sj] = True
    q = deque()
    q.append([si, sj])

    # 갖고 온 color가 Blue 일 때
    if color == 'B':
        while q:
            ci, cj = q.popleft()
            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color and not rg_visited[ni][nj]:
                    rg_visited[ni][nj] = True
                    q.append([ni, nj])

    # 갖고 온 color가 Blue가 아닐 때
    else:
        while q:
            ci, cj = q.popleft()
            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 'B' and not rg_visited[ni][nj]:
                    rg_visited[ni][nj] = True
                    q.append([ni, nj])
        

N = int(input().strip())
arr = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
rg_visited = [[False] * N for _ in range(N)]
# 적록색약은 R, G 구분을 못함 즉 같은것.
color_cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        color = arr[i][j]
        colorcheck(i, j)
        color_cnt += 1

red_green = 0
for i in range(N):
    for j in range(N):
        if rg_visited[i][j]:
            continue
        color = arr[i][j]
        rgcheck(i, j)
        red_green += 1

print(color_cnt, red_green)