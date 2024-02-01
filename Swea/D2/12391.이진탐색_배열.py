import sys
sys.stdin = open('2jin.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    start = 1
    end = P
    cntA = 0
    while start <= end:
        cntA += 1
        middle = (start + end) // 2
        if Pa == middle:
            break
        elif Pa > middle:
            start = middle
        elif Pa < middle:
            end = middle

    start = 1
    end = P
    cntB = 0
    while start <= end:
        cntB += 1
        middle = (start + end) // 2
        if Pb == middle:
            break
        elif Pb > middle:
            start = middle
        elif Pb < middle:
            end = middle
    
    if cntA < cntB:
        winner = 'A'
    elif cntA > cntB:
        winner = 'B'
    else:
        winner = '0'

    
    print(f'#{tc} {winner}')