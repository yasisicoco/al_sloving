from collections import deque

def bfs(si, sj):
    di = [0, 1, -1, 0]
    dj = [1, 0, 0, -1]
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = True # 방문처리
                q.append([ni, nj])

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())

    # 배추맵
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        arr[r][c] = 1
    # 배추방문맵
    visited = [[False] * M for _ in range(N)]

    cabage = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cabage += 1
    print(cabage)