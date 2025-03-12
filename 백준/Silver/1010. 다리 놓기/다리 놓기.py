tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    arr = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0:
                arr[i][j] = 0
            elif i == 1:
                arr[i][j] = j
            elif i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = sum(arr[i-1][1:j])

    print(arr[N][M])