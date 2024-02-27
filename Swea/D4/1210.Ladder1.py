# state1

# import sys
# sys.stdin = open('swea\\input\\1210.txt', 'r')
# sys.stdin = open('al_sloving\\swea\\input\\1210.txt', 'r')

# 방향 벡터설정
di = [0, 0, -1] # 우 좌 상
dj = [1, -1, 0]

def dfs(i, j):
    global result
    # 우, 좌
    for k in range(2): 
        ni = i + di[k]
        nj = j + dj[k]
        # ni, nj 가 배열 안에 있고 첫 방문일 때, 좌우 먼저 확인
        if 0 <= ni < 100 and 0 <= nj < 100 and not visited[ni][nj] and arr[ni][nj] == 1:
            visited[ni][nj] = True # 방문처리
            dfs(ni, nj)
    
    # 좌우에 길이 없을 때
    # 위로 가기
    # ni, nj가 배열안에 있다는 가정 하에 위로 가서 다시 dfs 진입 후 좌우 확인 > 반복
    ni = i + di[2] # 위로
    nj = j + dj[2]
    if 0 <= ni < 100 and 0 <= nj < 100 and not visited[ni][nj] and arr[ni][nj] == 1:
        visited[ni][nj] = True
        if ni == 0: # 세로 인덱스가 0 일 때,
            if result == -1: 
                result = nj
            return
        else:
            dfs(ni, nj)
    

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    visited = [[False] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                si = i
                sj = j
                # print(si, sj)
                break # 시작점 찾기
    
    result = -1
    visited[si][sj] = True # 시작점 방문처리
    dfs(si, sj) # 2번에서 출발
    print(f'#{tc} {result}')