import sys, copy
# from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 방향 벡터
di = [0, 1, 0, -1] # 우 하 좌 상
dj = [1, 0, -1, 0]

# 바이러스 퍼뜨리기
def virus(arr_deep):
    
    for i in range(N):
        for j in range(M):
            if arr_deep[i][j] == 2:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0 <= ni < N and 0 <= nj < M and arr_deep[ni][nj] == 0 and arr_deep[ni][nj] != 2:
                        arr_deep[ni][nj] = 2
                        virus(arr_deep)
    
    global answer
    cnt = 0
    for i in range(N):
        cnt += arr_deep[i].count(0)
    answer = max(answer, cnt)
        
# 안전지대 벽세우기
def wall(cnt):
    global arr

    if cnt == 3:
        arr_deep = copy.deepcopy(arr)
        virus(arr_deep)
        return
        
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0: # 0 이면
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

#---------------------------------------------------------------------
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
wall(0)
print(answer)