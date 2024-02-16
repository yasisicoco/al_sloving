# import sys
# sys.stdin = open('swea\\input\\11652.txt', 'r')

def bfs(si, sj):
    global goal_i, goal_j
    q = []
    q.append([si, sj])
    visited[si][sj] = 1

    while q: # 큐에 위치가 있는동안 실행
        ci, cj = q.pop(0)
        for k in range(4):
            ki = ci + di[k]
            kj = cj + dj[k]
            if 0 <= ki < N and 0 <= kj < N:
                if maze[ki][kj] == 0 and visited[ki][kj] == 0: # 미로가 0이고 처음가는 길
                    q.append([ki, kj])
                    visited[ki][kj] = 1 + visited[ci][cj]
                if ki == goal_i and kj == goal_j:
                    visited[ki][kj] = 1 + visited[ci][cj]
                    return visited[ki][kj] - 2 # 칸 수를 구하는 거라, 처음 1과 마지막 3밟은거 빼줌
    return 0 

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]       

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
    
    print(f'#{tc} {bfs(start_i, start_j)}')



