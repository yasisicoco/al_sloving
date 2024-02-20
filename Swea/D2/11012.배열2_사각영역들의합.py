T = int(input())    
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    sumone = 0
    for _ in range(M):
        mini_i, mini_j, r = map(int, input().split())
    
        for i in range(mini_i, mini_i+r):
            for j in range(mini_j, mini_j+r):
                if 0 <= i < N and 0 <= j < N:
                    sumone += arr[i][j]
                    arr[i][j] = 0

    print(f'#{tc} {sumone}')
