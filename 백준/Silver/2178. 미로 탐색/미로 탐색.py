def bfs(si, sj):
    global N, M
    Queue = []
    Queue.append((si, sj))
    visited[0][0] = 1
    
    while Queue:
        ci, cj = Queue.pop(0)
        for k in range(4):
            ki = ci + di[k]
            kj = cj + dj[k]
            if 0 <= ki < N and 0 <= kj < M:
                if arr[ki][kj] == 1 and visited[ki][kj] == 0:
                    visited[ki][kj] = visited[ci][cj] + 1
                    Queue.append((ki, kj))
                    if ki == (N-1) and kj == (M-1):
                        print(visited[ki][kj])
                        break


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start_i, start_j = (0, 0) # 시작점 설정
bfs(start_i, start_j)