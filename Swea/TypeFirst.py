# import sys; sys.stdin = open('1.txt', 'r')

from collections import deque

def func():
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    def is_vaild(r, c):
        return 0 <= r < N and 0 <= c < M
    
    def bfs(l):
        Q = deque()
        Q.append((sr, sc))
        visited = [[0] * M for _ in range(N)]
        visited[sr][sc] = 1

        while Q:
            r, c = Q.popleft()

            for k in range(4):
                if k == 0 or k == 2:
                    L = l
                else:
                    L = 1

                for dl in range(1, 1 + L):
                    nr, nc = r + dl * dr[k], c + dl * dc[k]

                    if not is_vaild(nr, nc) or visited[nr][nc] or not field[nr][nc]:
                        continue

                    if field[nr][nc] == 3:
                        return True

                    visited[nr][nc] = 1
                    Q.append((nr, nc))

        return False
    
    l = 1
    while not bfs(l):
        l += 1
    
    return l

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())    
    field = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if field[r][c] == 2:
                sr, sc = r, c

    print(f'#{tc} {func()}')