#state 1
# 방향벡터
di = [-1, 1, 0, 0, -1, -1, 1, 1] # 위 아래 좌 우 대각 2143
dj = [0, 0, 1, -1, -1, 1, 1, -1]

def oselo(i, j, P):
    
    for k in range(8): # 방향설정
        for l in range(1, N+1): # 뻗어나가며 확인
            ni = i + di[k] * l
            nj = j + dj[k] * l
            
            #다른 색 돌일때 
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != P and arr[ni][nj]!= 0:
                continue
            #같은 색 돌일때 끝좌표를 변수설정
            elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == P and arr[ni][nj]!= 0:
                ei, ej = ni, nj

                # 같은 색 돌로 바꾸기
                u = 1
                si = i
                sj = j
                while True:
                    if si == ei and sj == ej:
                        break
                    else:
                        si = i + di[k] * u
                        sj = j + dj[k] * u
                        arr[si][sj] = P
                    u += 1
                break
            else:
                break

    # print(i, j, P)
    # for line in arr:
    #     print(*line)
    # print()

T = int(input())
for tc in range(1, T+1):
    # N: 변의길이, M: 돌을 놓는 횟수
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)] 
    
    # 시작지점 설정 N = 0~3
    arr[N//2-1][N//2-1], arr[N//2][N//2] = 2, 2
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1
    # print(arr)
    # 행, 열, 1:흑 2:백
    for _ in range(M): # M번 돌을 놓는다.
        r, c, P = map(int, input().split()) # r, c 는 인덱스 -1 해줘야함
        r-=1
        c-=1
        arr[r][c] = P
        oselo(r, c, P)

    pr1 = 0
    pr2 = 0
    for line in arr:
        pr1 += line.count(1)
        pr2 += line.count(2)
    # print(arr)
    print(f'#{tc} {pr1} {pr2}')