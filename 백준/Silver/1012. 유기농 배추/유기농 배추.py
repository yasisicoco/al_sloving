import sys
sys.setrecursionlimit(10**6)

def dus(i, j):
    
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and not visited[ni][nj]:
            visited[ni][nj] = True
            dus(ni, nj)

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    
    cnt = 0 
    for l in range(N): # 그래프탐색
        for k in range(M):
            if arr[l][k] == 1 and not visited[l][k]: # 1이고 방문하지 않은곳
                visited[l][k] = True
                cnt += 1  # 카운트 +1
                dus(l, k) # 재귀로 주변 1을 돌면서 전부 방문처리
                
    print(cnt)