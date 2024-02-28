T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    
    s = e = N // 2

    sumone = 0
    for i in range(N):
        for j in range(s, e+1):
            sumone += int(arr[i][j])

        if i < N // 2: # 중간을 기준으로 위에 있으면
            s, e = s-1, e+1 # 범위를 넓힘
        else: # 중간을 기준으로 아래이면
            s, e = s+1, e-1 # 범위를 줄임

    print(f'#{tc} {sumone}')