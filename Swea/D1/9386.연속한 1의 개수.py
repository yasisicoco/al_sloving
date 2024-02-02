import sys
sys.stdin = open('literable1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = input()
    cnt = 0
    result = 0
    for i in lst:
        if i == '1':
            cnt += 1
            if cnt >= result:
                result = cnt
        else:
            cnt = 0
    print(f'#{tc} {result}')