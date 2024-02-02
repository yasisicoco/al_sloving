import sys
sys.stdin = open('gansobuun.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while N > 1:
        if N % 2 == 0:
            N = N // 2
            a += 1
        elif N % 3 == 0:
            N = N // 3
            b += 1
        elif N % 5 == 0:
            N = N // 5
            c += 1
        elif N % 7 == 0:
            N = N // 7
            d += 1
        elif N % 11 == 0:
            N = N // 11
            e += 1
    result.extend([a, b, c, d, e])

    print(f'#{tc}', *result)