di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def shot(i, j, bomb):
    # 첫 폭발지점을 가져와서 더해주기
    global cnt
    
    # 폭발 범위
    for l in range(1, bomb+1):
        for k in range(4):
            ni = i + di[k] * l
            nj = j + dj[k] * l

            # 영역 안에 있다면
            if 0 <= ni < N and 0 <= nj < N:
                cnt += arr[ni][nj] # 더해주기
                arr[ni][nj] = 0 # 폭발지점 사망자 지우기

T = int(input())
for tc in range(1, T+1):
    # N*N 영역, M개의 폭탄
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 사망한 적군
    cnt = 0

    # 폭탄 수 만큼 폭발
    for _ in range(M):
    # 폭발 위치(행, 열)와 범위
        r, c, bomb = map(int, input().split())
        cnt += arr[r][c] # 첫 폭발지점의 사망자
        arr[r][c] = 0 # 사망자 지우기
        shot(r, c, bomb)

    print(f'#{tc} {cnt}')