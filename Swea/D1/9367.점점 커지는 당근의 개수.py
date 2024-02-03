T = int(input())    
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split())) + [0]
    cnt = 1
    result = 1
    for i in range(N):
        if C[i] < C[i+1]:
            cnt += 1
            result < cnt
            result = cnt
        else:
            cnt = 1
    print(f'#{tc} {result}')