T = int(input())    
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    sumone = 0
    for _ in range(M):
        mini_i, mini_j, leng = map(int, input().split())
    
        for i in range(mini_i, N):
            for j in range(mini_j, N):
                if 0 <= i+leng < N and 0 <= j+leng < N:
                    sumone += arr[i][j]
                    arr[i][j] = 0

    print(f'#{tc} {sumone}')