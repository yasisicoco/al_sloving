T = int(input())
for tc in range(1, T+1):
    # N: 높이, M: 종류
    N, M = map(int, input().split())
    
    if M == 1:
        print(f'#{tc}')
        for i in range(1, N+1):
            print('*'*i)
    if M == 2:
        print(f'#{tc}')
        for i in range(N, 0, -1):
            print('*'*i)
    if M == 3:
        print(f'#{tc}')
        for i in range(1, N+1):
            print(' '*(N-i), end='')
            print('*'*(i-1), end=''); print('*', end=''); print('*'*(i-1), end='')
            print(' '*(N-i))