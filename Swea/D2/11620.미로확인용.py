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