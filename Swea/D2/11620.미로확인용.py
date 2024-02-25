import sys
sys.stdin = open('11620.txt', 'r')

def maze(start_i, start_j):
 
    global result
 
    for k in range(4):
        new_i = start_i + di[k]
        new_j = start_j + dj[k]
 
        if 0 > new_i or N <= new_i or 0 > new_j or N <= new_j:
            continue
        elif int(v[new_i][new_j]) == 0 and visited[new_i][new_j] == 0:
            visited[new_i][new_j] = 1
            maze(new_i, new_j)
        elif int(v[new_i][new_j]) == 3:
            result = 1
            return result
    return result
 
T = int(input())
 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
for tc in range(1, T+1):
    N = int(input())
    v = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
 
    for i in range(N):
        for j in range(N):
            if int(v[i][j]) == 2:
                start_i = i
                start_j = j
                break
     
    print(f'#{tc} {maze(start_i, start_j)}')


# state 2
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]


def dus(i, j):
    global result 
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        # 범위 안이고 1이 아니면,
        if 0 > ni or N <= ni or 0 > nj or N <= nj:
            continue
        elif arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dus(ni, nj)
        elif arr[ni][nj] == 3:
            result = 1
            return result
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 시작점 찾기
                si = i
                sj = j
                break
    dus(si, sj)
    print(f'#{tc} {result}')