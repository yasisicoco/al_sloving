import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [-1, 0, 1, 0] # 북 서 남 동
dj = [0, 1, 0, -1]

def clean(si, sj, dir_):
    global cnt

    while True:
        clean = 0    
        for _ in range(4):
            dir_ = (dir_+3) % 4
            ni = si + di[dir_]
            nj = sj + dj[dir_]

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                if visited[ni][nj] == False:
                    visited[ni][nj] = True
                    cnt += 1
                    si = ni
                    sj = nj
                    clean = 1
                    break
                
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우(다 방문한 경우)
        if clean == 0:
            if arr[si-di[dir_]][sj-dj[dir_]] == 1: # 벽인 경우
                print(cnt)
                break
            else: # 벽이 아닌 경우
                si, sj = si-di[dir_], sj-dj[dir_]



N, M = map(int, input().split())
r, c, dir_ = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt = 1
visited[r][c] = True
clean(r, c, dir_)