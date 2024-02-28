T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [False for _ in range(N)]

    path = [] # 신청서
    for _ in range(N):
        a, b = map(int, input().split())
        path.append((a, b))
    
    cnt = 1
    path.sort(reverse=True) # 시작 시간이 빠른것부터
    # print(path)
    for i in range(N): 
        if i == 0:
            start = path[i][0] #23
            end = path[i][1] #24
        else:
            if start >= path[i][1]:
                end = path[i][1]
                cnt += 1
                start = path[i][0]

    print(f'#{tc} {cnt}')