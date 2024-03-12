from collections import deque
import sys
import copy
input = sys.stdin.readline

# 방향 벡터
di = [0, 1, 0, -1] # 우 하 좌 상
dj = [1, 0, -1, 0]

# 바이러스 퍼뜨리기
def virus():
    arr_deep = copy.deepcopy(arr)
    Q = deque()

    # bfs
    for i in range(N):
        for j in range(M):
            if arr_deep[i][j] == 2:
                Q.append((i, j))
    
    while Q:
        r, c = Q.popleft()

        for k in range(4):
            ni = r + di[k]
            nj = c + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if arr_deep[ni][nj] == 0:
                arr_deep[ni][nj] = 2
                Q.append((ni, nj))

    
    global answer
    cnt = 0
    for i in range(N):
        cnt += arr_deep[i].count(0)
    answer = max(answer, cnt)
        
# 안전지대 벽세우기
def wall(cnt):
    if cnt == 3:
        virus()
        return
        
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: # 0 이면
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
wall(0)

print(answer)