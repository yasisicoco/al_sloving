def dfs(x,y):
    global ans
    # visited[x][y] = 1

    if x == m - 1 and y == n - 1:
        ans = 'Yes'
        return

    for k in range(2):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] != 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
di = [0, 1]  # 우,하 방향설정
dj = [1, 0]
ans = 'No'

dfs(0, 0)
print(ans)