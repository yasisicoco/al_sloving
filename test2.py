from collections import deque

di = [1, 1, 1]
dj = [-1, 0, 1]

def bfs(si):
    global result

    q = deque()
    sumone = arr[0][si]
    q.append([0, si, sumone, -1])

    while q:
        ci, cj, sumone, dir = q.popleft()
        for k in range(3):
            ni = ci + di[k]
            nj = cj + dj[k]
            if dir == dj[k]:
                continue
            if 0 <= ni < N and 0 <= nj < M:
                if ni == N-1:
                    sumone += arr[ni][nj]
                    result = min(sumone, result)
                    continue
                q.append([ni, nj, sumone+arr[ni][nj], dj[k]])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 10e9
for i in range(M):
    bfs(i)

print(result)