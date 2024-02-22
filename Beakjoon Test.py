import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i, j):
    global cnt

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
    
        # ni, nj가 행렬 안에 있고 방문하지 않았고 사람이 있는 곳이며 벽이 아니라면
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 'P' and arr[ni][nj] != 'X':
            visited[ni][nj] = True # 방문처리
            cnt += 1
            dfs(ni, nj)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [input() for _ in range(N)] # 문자열 한줄로넣어서 M이 필요없음

# 인접행렬
# v = [[] * M for _ in range(N)]
# 방문리스트
visited = [False * M for _ in range(N)]

cnt = 0 # 사람 만난 횟수
for i in range(N):
    for j in range(M):
        # 방문한적 없고 도연이가 있는 곳에서 시작, 벽은 피하기
        if not visited[i][j] and arr[i][j] == 'I' and arr[i][j] != 'X': 
            visited[i][j] = True # 도연이가 있는곳을 방문처리
            dfs(i, j) # 움직이러 고고

print(cnt)