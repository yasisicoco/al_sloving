# 고려해야할 것
# 1. 가로에 1~9가 한개씩 들어가있는지?
# 2. 세로에 1~9가 한개씩 들어가있는지?
# 3. 3x3 에 1~9가 한개씩 들어가있는지?

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    # 가로 x 세로
    result = 0
    for i in range(9):
        sumi = 0
        sumj = 0
        for j in range(9):
            sumj += arr[i][j] # 가로줄 확인
            sumi += arr[j][i] # 세로줄 확인
        if sumj == 45:
            result += sumj
        else:
            break           # 중간에 틀리면 끝
            
        if sumi == 45:
            result += sumi
        else:
            break


    sumk = 0
    for k in range(9):
        for l in range(9):
            if 0 <= k <= 2 and 0 <= l <= 2: # 1
                sumk += arr[k][l]
    if sumk == 45:
        result += sumk

    sumk1 = 0
    for k in range(9):
        for l in range(9):
            if 0 <= k <= 2 and 3 <= l <= 5: # 2
                sumk1 += arr[k][l]
    if sumk1 == 45:
        result += sumk1

    sumk2 = 0
    for k in range(9):
        for l in range(9):
            if 0 <= k <= 2 and 6 <= l <= 8: # 3
                sumk2 += arr[k][l]
    if sumk2 == 45:
        result += sumk2

    sumk3 = 0
    for k in range(9):
        for l in range(9):
            if 3 <= k <= 5 and 0 <= l <= 2: # 4
                sumk3 += arr[k][l]
    if sumk3 == 45:
        result += sumk3

    sumk4 = 0
    for k in range(9):
        for l in range(9):
            if 3 <= k <= 5 and 3 <= l <= 5: # 5
                sumk4 += arr[k][l]
    if sumk4 == 45:
        result += sumk4

    sumk5 = 0
    for k in range(9):
        for l in range(9):
            if 3 <= k <= 5 and 6 <= l <= 8: # 6
                sumk5 += arr[k][l]
    if sumk5 == 45:
        result += sumk5

    sumk6 = 0
    for k in range(9):
        for l in range(9):
            if 6 <= k <= 8 and 0 <= l <= 2: # 7
                sumk6 += arr[k][l]
    if sumk6 == 45:
        result += sumk6

    sumk7 = 0
    for k in range(9):
        for l in range(9):
            if 6 <= k <= 8 and 3 <= l <= 5: # 8
                sumk7 += arr[k][l]
    if sumk7 == 45:
        result += sumk7

    sumk8 = 0
    for k in range(9):
        for l in range(9):
            if 6 <= k <= 8 and 6 <= l <= 8: # 9
                sumk8 += arr[k][l]
    if sumk8 == 45:
        result += sumk8

    if result == 1215:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')