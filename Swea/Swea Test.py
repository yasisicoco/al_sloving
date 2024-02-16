def bfs(si, sj):
    q = []
    q.append(maze[si][sj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 방문 리스트
    visited = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N): # 시작과 끝 찾기
        for j in range(N):
            if maze[i][j] == 2:
                start_i = i
                start_j = j
            elif maze[i][j] == 3:
                goal_i = i
                goal_j = j
                break
    
    bfs(start_i, start_j)