import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

di = [0, 1, -1, 0, 0]
dj = [1, 0, 0, -1, 0]

def check(si, sj, visited):
    for k in range(5):
        ni = si + di[k]
        nj = sj + dj[k]
        if not ((0 <= ni < N and 0 <= nj < N) and visited[ni][nj]):
            return False
    return True

def seedsum(si, sj):
    seed = 0
    for k in range(5):
        ni = si + di[k]
        nj = sj + dj[k]
        seed += arr[ni][nj]
    return seed

def recur(si, cnt, visited, sumone):
    global result
    if cnt == 3:
        result = min(sumone, result) # 최대값 저장
        return
    # 가로배열 값을 1씩 더해서 순회한 것을 받아오기
    for i in range(si, N-1):
        for j in range(1, N-1):
            if check(i, j, visited):
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = False
                # 백트래킹
                recur(i, cnt+1, visited, sumone+seedsum(i, j))
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = True

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[True] * N for _ in range(N)]
# 테두리 안쪽을 돈다.

result = 10e9
# 가로 인덱스값, 꽃잎 갯수, 방문값, 꽃잎 가격
recur(1, 0, visited, 0)
print(result)