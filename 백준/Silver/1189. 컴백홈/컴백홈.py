di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def dfs(si, sj, cnt):
    global ans
    
    if arr[si][sj] == 'end':
        ans.append(cnt)
        
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]

        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] != 'T':
            visited[ni][nj] = True
            dfs(ni, nj , cnt+1)
            visited[ni][nj] = False

R, C, K = map(int, input().split())
arr = [[] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]

for i in range(R):
    str_val = input()
    for j in range(C):
        arr[i].append(str_val[j])

arr[R-1][0] = 'start'
arr[0][-1] = 'end'

visited[R-1][0] = True
ans = []

dfs(R-1, 0, 1)
print(ans.count(K))