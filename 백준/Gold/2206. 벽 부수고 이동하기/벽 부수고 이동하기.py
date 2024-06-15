from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# 3차원 배열로 vis를 선언: [벽 부수지 않은 경우][벽 부순 경우]
vis = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs(si, sj):
    global result
    
    q = deque()
    q.append([si, sj, 1, 0])
    vis[si][sj][0] = 1
    
    while q:
        ci, cj, cnt, wallbreak = q.popleft()
        
        # 도착했을 때
        if ci == N-1 and cj == M-1:
            result = min(cnt, result)
            continue
            
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                # 만약 그냥 통로라면
                if arr[ni][nj] == '0' and vis[ni][nj][wallbreak] == 0:
                    vis[ni][nj][wallbreak] = 1
                    q.append([ni, nj, cnt+1, wallbreak])
                # 만약 벽(1) 일 때, 아직 부순적이 없다면
                if arr[ni][nj] == '1' and wallbreak == 0 and vis[ni][nj][1] == 0:
                    vis[ni][nj][1] == 1
                    q.append([ni, nj, cnt+1, 1])

result = 10e9
bfs(0, 0)

# 도착지점에 못 갔을 때
if result == 10e9:
    print(-1)
else:
    print(result)