    # path[0] : 회사
        # 중간에 고객 2, 3, 4, 5, ..., N+1
    # path[1] : 집

# D5. 최적 경로. 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    path = []
    for i in range(0, (N+2)*2, 2):
        a, b = arr[i], arr[i+1]
        path.append((a, b))
    
    print(path)

    v = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(j+1, N):
            v[j][k] = abs(path[j][0]-path[k][0]) + abs(path[j][1]-path[k][1])
            v[k][j] = v[j][k]

    for line in v:
        print(line)    

    # ans = 0
    # gohome(path[0][0], path[0][1], 0) # 회사의 x좌표, y좌표, 최소값

    

