def W_color(si, sj):
    global min_val

    ni = si
    nj = sj + 1

    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'W':
        min_val += 1
        W_color(ni, nj)
    elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'W':
        W_color(ni, nj)

def B_color(si, sj):
    global min_val

    ni = si
    nj = sj + 1

    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'B':
        min_val += 1
        B_color(ni, nj)
    elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'B':
        B_color(ni, nj)

def R_color(si, sj):
    global min_val

    ni = si 
    nj = sj + 1

    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'R':
        min_val += 1
        R_color(ni, nj)
    elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'R':
        R_color(ni, nj)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    
    arr = [list(input()) for _ in range(N)]

    # WHITE
    # BLUE
    # RED
    result = 10**99
    for i in range(N-2):
        min_val = 0 # 개수 카운트
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                W_color(i, 0)
                B_color(j, 0)
                R_color(k, 0)
        if result >= min_val:
            result = min_val
    print(result)