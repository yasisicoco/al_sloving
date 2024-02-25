import sys
sys.stdin = open('swea\\input\\1210.txt', 'r')

# 방향 벡터설정
di = [0, 0, 1, -1] # 우 좌 하 상
dj = [1, -1, 0, 0]

def dfs(i, j):

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        pass
        # if arr[ni][nj]

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    visited = [[False] * 100 for _ in range(100)]
    print(visited)

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                si = i
                sj = j
                break # 시작점 찾기
    
    # dfs(si, sj)