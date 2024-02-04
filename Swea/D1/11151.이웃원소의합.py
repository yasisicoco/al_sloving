# import sys
# sys.stdin = open('D1이웃원소의합.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    result = 0
    maxnum = 0
    for i in range(N): # 0~4
        if 0 <= i < N and i+1 < N:
            result = maxnum
            result = lst[i] + lst[i+1]
        if maxnum < result:
            maxnum = result
    print(f'#{tc} {maxnum}')