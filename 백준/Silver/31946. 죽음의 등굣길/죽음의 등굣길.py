from collections import deque

def bfs():
    visited[0][0] = True
    q = deque([(0, 0)])
    
    while q:
        ci, cj = q.popleft()
        
        # 목적지에 도착한 경우
        if ci == N-1 and cj == M-1:
            print("ALIVE")
            return
        
        for di in range(-X, X+1):
            for dj in range(-X, X+1):
                if abs(di) + abs(dj) > X:
                    continue
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == arr[ci][cj]:
                    visited[ni][nj] = True
                    q.append((ni, nj))
    
    # 목적지에 도달할 수 없는 경우
    print("DEAD")

# 입력 부분
N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
X = int(input())

visited = [[False] * M for _ in range(N)]

start = arr[0][0] # 첫 보도블럭 색

if start != arr[-1][-1]:
    print("DEAD")
else:
    bfs()
