import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(i, j):
    global cnt

    for k in range(4): # 방향 벡터 설정
        ni = i + di[k]
        nj = j + dj[k]
    
        # ni, nj가 행렬 안에 있고 방문하지 않았고 사람이 있는 곳이며 벽이 아니라면
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != 'X':
            visited[ni][nj] = True # 방문처리
            if arr[ni][nj] == 'P': # 사람만났을때
                cnt += 1
            dfs(ni, nj) # 방문한 곳에서 다시 주변탐색

N, M = map(int, input().split())
arr = [input() for _ in range(N)] # 문자열 한줄로넣어서 M이 필요없음

# 인접행렬
# v = [[] * M for _ in range(N)]
# 방문리스트
visited = [[False] * M for _ in range(N)]
cnt = 0 # 사람 만난 횟수
for i in range(N): # 3
    for j in range(M): # 5
        # 방문한적 없고 도연이가 있는 곳에서 시작, 벽은 피하기
        if arr[i][j] == 'I': 
            visited[i][j] = True # 도연이가 있는곳을 방문처리
            si = i
            sj = j
            break

dfs(si, sj) # 움직이러 고고

if cnt != 0: # 사람을 만났다면
    print(cnt) # cnt 출력
else:
    print('TT') # 못만났다면 TT