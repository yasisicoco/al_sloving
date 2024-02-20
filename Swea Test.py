T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    A = []
    cnt = 0
    real = 0
    for _ in range(1, 13):
        A.append(_)
        cnt += 1
        if cnt == N:
            result = sum(A)
            if result == K:
                real += 1
    print(f'#{tc} {real}')