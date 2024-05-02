di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def seedsum(si, sj):
    global visited, arr
    seed = arr[si][sj]
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if visited[ni][nj]:
            return 
        visited[ni][nj] = True
        seed += arr[ni][nj]

def recur(si):
    global visited
    visited = [[False] * N for _ in range(N)]
    for k in range(si, N-1):

        cnt = 0
        for i in range(1, N-1):
            for j in range(i, N-1):
                if not visited[k][j]:
                    min_val = seedsum(k, j)
                    cnt += 1
                    if cnt == 3:
                        result = min(min_val, result)
                        continue

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 테두리 안쪽을 돈다.
# visited가 겹치면 바로 리턴한다.

result = 10e9
for i in range(1, N-1):
    recur(i)

print(result)