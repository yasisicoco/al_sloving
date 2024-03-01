T = int(input())
for tc in range(1, T+1):
    # 행, 열, 크기N
    r, c, N = map(int, input().split())
    arr = [[0] * 10 for _ in range(10)]

    

    print(f'#{tc}')
    for line in arr:
        print(*line)