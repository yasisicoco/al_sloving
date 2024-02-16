import sys
sys.stdin = open('swea\\input\\1226.txt', 'r')
# sys.stdin = open('../input/1226.txt', 'r')

def bfs(start_i, start_j):
    global end_i, end_j
    q = []
    q.append([start_i, start_j])
    visited[start_i][start_j] = 1

    while q:
        ci, cj = q.pop(0)
        for k in range(4):
            ri = ci + di[k]
            rj = cj + dj[k]
            if 0 <= ri < N and 0 <= rj < N:
                if maze[ri][rj] == 0 and visited[ri][rj] == 0:
                    q.append([ri, rj])
                    visited[ri][rj] = 2
                if ri == end_i and rj == end_j: # 도착조건
                    return 1


    return 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

T = 10
for _ in range(T):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    # 방문리스트
    visited = [[0] * (N+1) for _ in range(N+1)] # 17*17

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i = i
                start_j = j
            if maze[i][j] == 3:
                end_i = i
                end_j = j
                break
    print(f'#{tc} {bfs(start_i, start_j)}')