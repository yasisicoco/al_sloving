import sys
sys.stdin = open('D1최대최소.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = [0]+list(map(int, input().split()))+[0]
    
    max_num = 0
    min_num = 9999999
    max_val = 0
    min_val = 0
    for i in range(1, N+1):
        if ai[i] >= max_num:
            max_num = ai[i]
            max_val = i
    for j in range(N, 0, -1):
        if ai[j] <= min_num:
            min_num = ai[j]
            min_val = j
    print(f'{tc} {abs(max_val-min_val)}')