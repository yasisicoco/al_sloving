dir = [-1, 0, 1]

def dfs(si, sj, n_dir, sumone):
    global result
    if si == N-1:
        result = min(sumone, result)
        return
    
    for i in dir:
        if n_dir == i:
            continue
        if 0 <= si < N and 0 <= sj+i < M:
            dfs(si+1, sj+i, i, sumone+arr[si+1][sj+i])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 10e9
for i in range(M):
    # 들고갈것. (세로인덱스, 가로인덱스, 방향값, 연료의 양)
    dfs(0, i, -2, arr[0][i])

print(result)