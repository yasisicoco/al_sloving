from collections import deque

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def bfs_w(si, sj):
    global W
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == 'W':
                visited[ni][nj] = True
                W += 1
                q.append([ni, nj])

def bfs_b(si, sj):
    global B
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == 'B':
                visited[ni][nj] = True
                B += 1
                q.append([ni, nj])
                

N, M = map(int, input().split())
arr = [input() for _ in range(M)]
visited = [[False] * N for _ in range(M)]

W_val = 0; B_val = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W' and not visited[i][j]:
            W = 1
            bfs_w(i, j)
            W_val += W**2
        elif arr[i][j] == 'B' and not visited[i][j]:
            B = 1
            bfs_b(i, j)
            B_val += B**2
            
print(W_val, B_val)