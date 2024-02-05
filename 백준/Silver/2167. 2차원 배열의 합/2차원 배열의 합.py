from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
K = int(stdin.readline())

for _ in range(K):
    i, j, x, y = map(int, stdin.readline().split())
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