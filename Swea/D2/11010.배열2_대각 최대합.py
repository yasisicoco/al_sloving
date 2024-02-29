di = [-1, -1, 1, 1]
dj = [-1, 1, 1, -1]

def cross(i, j):

    # i, j에서시작하여 대각선의 총합
    sumone = arr[i][j]
    for l in range(1, N*2+1): # 배열의 크기 *2
        for k in range(4): # 대각선 4방향
            ni = i + di[k] * l
            nj = j + dj[k] * l

            if 0 <= ni < N and 0 <= nj < N: # 배열 안에있다는 조건
                sumone += arr[ni][nj]

    return sumone # 대각선의 총합

T = int(input())    
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N): # 완전탐색
        for j in range(N):
            sumone = cross(i, j) # 대각선 총합을 들고나옴
            if result <= sumone: # 함수를 돌고나와서 대각선 총합이 클 때마다 갱신
                result = sumone
    
    print(f'#{tc} {result}')