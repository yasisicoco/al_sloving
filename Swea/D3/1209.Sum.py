# import sys
# sys.stdin = open('Sum.txt')
# 
# T = 10
# for _ in range(1, T + 1):
    # tc = int(input())
    # tmi = [list(map(int, input().split())) for _ in range(100)]
    # lst = []
    # for r in range(100):
        # for c in range(100):
            # if r == c:
                # result01 += tmi[r][c]
            # if r + c == 99:
                # result02 += tmi[c][r]
# 
    # result03 = 0
    # result04 = 0
    # winner = 0
    # 행 합 / 열 합
    # for r in range(100):
        # for c in range(100):
            # result03 += tmi[r][c]
            # result04 += tmi[c][r]
    # if result03 <= result04:
        # winner = result04
    # else:
        # winner = result03
# 
    # lst.append(result01)
    # lst.append(result02)
    # lst.append(winner)
    # lst.sort()
    # result = lst[-1]
    # print(f'#{tc} {result}')
    # winner = 0



# 2차 시도
import sys
sys.stdin = open('Sum.txt')

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    tmi = [list(map(int, input().split())) for _ in range(100)]

    # 열의 합
    sum01 = 0
    for r in range(100):
        result = 0
        for c in range(100):
            result += tmi[r][c]
        if sum01 <= result:
            sum01 = result
    # print(sum01)

    # 행의 합
    sum02 = 0
    for r in range(100):
        result = 0
        for c in range(100):
            result += tmi[c][r]
        if sum02 <= result:
            sum02 = result
    # print(sum02)

    # 대각선합
    sum03 = 0
    for c in range(100):
        result01 = 0
        result02 = 0
        result01 += tmi[c][c] # 정방향 대각선
        result02 += tmi[c][99-c] # 역방향 대각선
        if max(result01, result02) >= sum03:
            sum03 = max(result01, result02)
    
    # print(sum03)
    print(f'#{tc} {max(sum01, sum02, sum03)}')