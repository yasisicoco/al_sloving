''' 
세울 수 있는 벽은 3개이며 무조건 3개를 세워야 한다.
연구소의 크기는 N*M 이다.

1. 0지역에 1로 벽 3개 세우기
2. 2와 인접한 0지역을 2로 채우기, 만약 1을 만나면 종료
3. 0인 지역 탐색하여 카운트하기
4. 카운트한 안전영역이 최대값이면 갱신
'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 방향 벡터
di = [0, 1, 0, -1] # 우 하 좌 상
dj = [1, 0, -1, 0]

# 바이러스 퍼뜨리기
def virus(vi, vj):
    
    for k in range(4):
        ni = vi + di[k]
        nj = vj + dj[k]

        if 0 <= ni < N and 0 <= nj < M and not visited_virus[ni][nj] and arr[ni][nj] == 0:
            visited_virus[ni][nj] = True
            arr[ni][nj] = 2
            virus(ni, nj)

# 안전지대의 수 세기
def safe(arr):
    safeZone = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safeZone += 1
    return safeZone

# 안전지대 벽세우기
def wall(start, cnt, num, arr):
    global zero, result, visited_recur
    if cnt == 3: # 벽 세개 세웠을 때
        # 재귀로 돌면서 세개 1로 바꿨을 때, 바이러스 유포
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    vi, vj = i, j # 바이러스 시작좌표
                    virus(vi, vj)
        ans = safe(arr) # 갱신코드
        if result <= ans:
            result = ans
        return 
            
    for i in range(start, num):
        if visited_recur[i] == True:
            continue
        a, b = zero[i]
        visited_recur[i] = True
        arr[a][b] = 1
        wall(start+1, cnt+1, num, arr)
        visited_recur = False
        arr[a][b] = 0

        
        
#---------------------------------------------------------------------
# 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())
# 연구소 지도
arr = [list(map(int, input().split())) for _ in range(N)]
visited_virus = [[False] * M for _ in range(N)] # 바이러스용 방문표시
arr_2 = arr[:]
zero = []
# 0인 좌표를 리스트에 넣기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero.append((i, j))

result = 0
zero = deque(zero) # 재귀 시작
num = len(zero)
visited_recur = [False] * (num+10) # 재귀용 방문표시
wall(0, 0, num, arr)

print(result)