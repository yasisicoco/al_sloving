T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            max = 0
            if 2 <= i+M <= N and 2 <= j+M <= N:
                for k in range(i, i+M):
                    for l in range(j, j+M):
                        max += arr[k][l]
                        if result <= max:
                            result = max
    
    print(f'#{tc} {result}')