''' 
세울 수 있는 벽은 3개이며 무조건 3개를 세워야 한다.
연구소의 크기는 N*M 이다.

1. 0지역에 1로 벽 3개 세우기
2. 2와 인접한 0지역을 2로 채우기, 만약 1을 만나면 종료
3. 0인 지역 탐색하여 카운트하기
4. 카운트한 안전영역이 최대값이면 갱신
'''
import sys
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

        if 0 <= ni < N and 0 <= nj < M and not visited_virus[ni][nj] and arr_2[ni][nj] == 0:
            visited_virus[ni][nj] = True
            arr_2[ni][nj] = 2
            virus(ni, nj)

# 안전지대의 수 세기
def safe(arr_2):
    safeZone = 0
    for i in range(N):
        for j in range(M):
            if arr_2[i][j] == 0:
                safeZone += 1
    return safeZone

# 안전지대 벽세우기
def wall(arr_2):
    cnt = 0 # 벽의 갯수
    for i in range(N):
        for j in range(M):
            if arr_2[i][j] == 0:
                arr_2[i][j] = 1
                cnt += 1
            if cnt == 3:
                break
        if cnt == 3:
            break
    return arr_2

# 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())
# 연구소 지도
arr = [list(map(int, input().split())) for _ in range(N)] 

result = 0 # 안전지대 검사
while True:
    visited_virus = [[False] * M for _ in range(N)] # 바이러스용 방문표시
    # 벽을 3개 세울 0(안전지대) 찾아서 세우기
    arr_2 = wall(arr)

    # 바이러스 찾아서 퍼뜨리기
    for i in range(N):
        for j in range(M):
            if arr_2[i][j] == 2:
                vi, vj = i, j # 바이러스 시작좌표
                virus(vi, vj)
    
    ans = safe(arr_2)
    if result <= ans:
        result = ans
    
print(ans)