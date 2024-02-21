from pprint import pprint

def dus(i, j):
    for dir in range(4):
        si = i + di[dir]
        sj = i + dj[dir]

        for i in range(N):
            for j in range(M):
                if 0 <= si < N and 0 <= sj < M and arr[si][sj] == 1 and not visited[si][sj]:
                    visited[si][sj] = True
                    dus(si, sj)

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    pprint(arr)
    pprint(visited)
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    
    cnt = 0
    for l in range(M):
        for k in range(N):
            if arr[k][l] == 0 and not visited[k][l]:
                visited[k][l] = True
                dus(k, l)
                cnt += 1
    print(cnt)