N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    cnt = 0
    for di in range(0, N):
        if i-1 <= di <= x-1:
            pass
        else:
            continue
        for dj in range(0, M):
            if j-1 <= dj <= y-1:
                cnt += arr[di][dj]
            else:
                continue
    print(cnt)