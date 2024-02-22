# 11315. 오목

# 구현으로 풀어보자
# 주어진 정수 N 은 오목판의 크기 (가로x세로)
# 문자열로 배열 만들기
# 포문 두개로 배열 돌면서 o 찾기
# 방향 벡터는 오른쪽, 아래, 오른대각,왼대각 만 찾자
# 찾은 o를 방향 벡터로 움직이면서 연속되는 오목알 5개를 찾으면 YES 후 브레이크
# 끝까지 못찾으면 NO

import sys
# sys.stdin = open('swea\\input\\11315.txt')
sys.stdin = open('al_sloving\\swea\\input\\11315.txt')
sys.setrecursionlimit(10 ** 6)

# 방향 벡터 설정
di = [0, 1, 1, 1] # 우 하 우하 좌하
dj = [1, 0, 1, -1]

def omok(arr):
    global cnt
    
    for i in range(N):
        for j in range(N):

            if arr[i][j] == 'o':
                for k in range(4): # 바로 돌지 않음
                    ni = i
                    nj = j
                    cnt = 0
                    # 연속?
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k] # while문에서 한방향으로 계속 돌기
                        nj += dj[k]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {omok(arr)}')