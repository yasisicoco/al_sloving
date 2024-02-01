T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * N for _ in range(N)]
    print(arr)
    r = 0
    c = 0
    k = 0
    for _ in range(3):
        for _ in range(N-1):
            r = r + dr[k]
            c = c + dc[k]
            arr[r][c] += 1
        k += 1
        if k >= 4:
            k -= 4
    for _ in range(2):
        for _ in range(N-1):
            r = r + dr[k]
            c = c + dc[k]
            arr[r][c] += 1
        k += 1
        if k >= 4:
            k -= 4
    print(f'#{tc} {arr}')