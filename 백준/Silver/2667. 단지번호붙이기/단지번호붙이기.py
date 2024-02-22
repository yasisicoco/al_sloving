# 연결되었다는 것은 위아래 혹은 좌우로 집이 있음. 대각선은 아님
# 1은 집이 있는곳, 0은 없는곳
# 각 단지에 속하는 집의 수, 오름차순 정렬

# 1. 방향 벡터 설정, 방문확인 설정, 방문 확인했을때 연결되어있다면 재귀 밖에서 카운트.
# 2. 다음 재귀로 들어갈 땐 카운트가 1 늘어남.
# 3. 마지막에 집 수를 한줄씩 오름차순으로 출력
from pprint import pprint
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 방향 벡터
di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

# 탐색
def dfs(i, j):
    global size

    for k in range(4): # 방향 벡터 설정
        ni = i + di[k]
        nj = j + dj[k]

        # ni, nj가 범위를 벗어나지 않고 첫 방문이며, 단지인 곳
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and v[ni][nj] == '1':
            visited[ni][nj] = True # 방문처리
            size += 1 # 같은 단지인 곳 카운트
            dfs(ni, nj)

# 첫번째 줄 지도의 크기 N
N = int(input())

# 단지 행렬, 문자열로 받음
v = [input() for _ in range(N)]

# 방문확인 리스트
visited = [[False for _ in range(N)] for _ in range(N)]

sizelst = [] # 단지 사이즈 비교용
for i in range(N):
    for j in range(N):
        size = 1 # 단지한번 다 돌고 사이즈 초기화
        if not visited[i][j]: # 첫 방문이라면
            visited[i][j] = True # 방문 체크
            if v[i][j] == '1': 
                dfs(i, j) # 단지 순회 시작
                sizelst.append(size)
            # break

sizelst.sort()
cnt = 0 # 단지 수
for e in sizelst: # 0이 아니라면 카운트 및 출력
    if e != 0:
        cnt += 1
print(cnt)
for e in sizelst: # 오름차순 순서대로 출력
    if e != 0:
        print(e)