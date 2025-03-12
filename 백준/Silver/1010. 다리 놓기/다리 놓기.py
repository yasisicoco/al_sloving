tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    arr = [[0] * (M+1) for _ in range(N+1)]

    for j in range(M+1):
        arr[1][j] = j
        
    for i in range(2, N+1):
        prev = [0] * (M+1)
        for j in range(M+1):
            prev[j] = prev[j-1] + arr[i-1][j]
        for j in range(i, M+1):
            arr[i][j] = prev[j-1]

    print(arr[N][M])