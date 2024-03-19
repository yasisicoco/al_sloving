import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [-1, 0, 1, 0] # 북 서 남 동
dj = [0, -1, 0, 1]

def clean(si, sj, dir_):
    global cnt

    if visited[si][sj] == False: # 현재 칸이 아직 청소되지 않은 경우
        visited[si][sj] = True # 청소
        cnt += 1
    
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if not visited[ni][nj] and arr[ni][nj] == 0: 
            clean(ni, nj, k) # 1번으로 돌아감
        elif visited[ni][nj]:
            continue

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우(다 방문한 경우)
    ni = si + di[(dir_+2) % 4] # 뒤를 본다
    nj = si + dj[(dir_+2) % 4]
    if arr[ni][nj] != 1: # 뒤가 벽이 아니고 방문하지 않았다면
        clean(ni, nj, dir_) # 1번으로 돌아감
    else: # 벽인 경우
        print(cnt)
        exit()

N, M = map(int, input().split())
r, c, dir_ = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt = 0
clean(r, c, dir_)
print(cnt)