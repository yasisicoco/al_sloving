from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def bfs():
    result = -1
    while q:
        si, sj = q.popleft()
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == -1:
                continue
            if 0 <= ni < N and 0 <= nj < M and day[ni][nj] == 0:
                day[ni][nj] += day[si][sj] + 1
                if day[si][sj] < day[ni][nj]:
                    result = day[ni][nj]
                q.append([ni, nj])
                
    return result

def already():
    result = 0 # 모두 익어있다면 바뀌지 않음
    for i in range(N):
        for j in range(M):
            if box[i][j] == -1:
                continue
            elif box[i][j] == 0:
                return # 모두 익어있는 상황이 아님
    
    return result

def ready():
    result = 0 # 모두 익어있다면 바뀌지 않음
    for i in range(N):
        for j in range(M):
            if box[i][j] == -1:
                continue
            elif day[i][j] == 0:
                result = -1 # 모두 익지 못하는 상황
    
    return result

''' --------------------------------------------------------------------'''

# N: 세로 / M: 가로
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 익는 날짜
day = [[0] * M for _ in range(N)]

# 모두 익어있는 상황
end = already()
if end == 0:
    print(0)
    exit()

# 토마토익히기
q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == -1:
            continue
        elif box[i][j] == 1:
            day[i][j] = 1
            q.append([i, j])

ans = bfs()
end_ = ready()
if end_ == -1:
    print(-1)
else:
    print(ans-1)