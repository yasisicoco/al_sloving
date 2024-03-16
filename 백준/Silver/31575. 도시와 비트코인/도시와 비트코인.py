di = [0, 1] # 오른쪽 아래쪽
dj = [1, 0]

def dfs(si, sj):
    global result 
    
    if si == M-1 and sj == N-1:
        result = 'Yes'
        return
        
    
    for k in range(2):
        ni = si + di[k]
        nj = sj + dj[k]

        if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 0:
            visited[ni][nj] = True
            dfs(ni, nj)            
        
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
visited[0][0]=True
result = 'No'
dfs(0,0)
print(result)