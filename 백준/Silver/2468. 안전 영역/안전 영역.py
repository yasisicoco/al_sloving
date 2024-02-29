import sys
sys.setrecursionlimit(10**6)

di = [0, 1, -1, 0]
dj = [-1, 0, 0, 1]

def dfs(si, sj):
    global high
    
    for k in range(4):
        ni = si + di[k]    
        nj = sj + dj[k]    
        
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and arr[ni][nj] > high:
            visited[ni][nj] = True
            dfs(ni, nj)
            
# 2차원 배열의 행과 열의 개수
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


result = 0
for high in range(0, 101): 
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            if arr[i][j] > high: # 비높이보다 높을 경우에만 방문표시
                visited[i][j] = True
                cnt += 1
                dfs(i, j)
            else: # 첫방문인데 잠겼을 경우 False 그대로
                continue
    visited = [[False] * N for _ in range(N)] # 높이 순회할때마다 방문값 초기화
    if result <= cnt:
        result = cnt
print(result)