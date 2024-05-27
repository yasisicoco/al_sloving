from collections import deque

# 방향 벡터
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

# BFS를 사용해 연합 찾기
def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    union = [(si, sj)] # 현재 연합에 포함된 국가들
    sumone = arr[si][sj] # 연합의 인구수 합계
    cnt = 1 # 연합을 이루는 국가의 수
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                dif = abs(arr[x][y] - arr[ni][nj])
                if L <= dif <= R:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
                    union.append((ni, nj))
                    sumone += arr[ni][nj]
                    cnt += 1
    for i, j in union:
        arr[i][j] = sumone // cnt # 연합의 인구 이동 처리
    return cnt > 1 # 연합을 이루는 국가가 2개 이상일 경우 True 반환

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    isMoved = False # 인구 이동이 일어났는지 체크
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if bfs(i, j):
                    isMoved = True
    if not isMoved:
        break
    day += 1

print(day)
