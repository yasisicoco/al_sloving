di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j, path):
    
    # 7자리가 되면 반환
    if len(path) == 7:
        result.add(path)
        return
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, path + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')