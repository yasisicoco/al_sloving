from heapq import heappush, heappop

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
INF = int(1e9)

def dijkstra(si, sj):

    pq = []
    distance[si][sj] = 0
    heappush(pq, (0, si, sj))

    while pq:
        height, ci, cj, dist = heappop(pq)
        
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if height > arr[ni][nj]:
                    height = arr[ni][nj]
                visited[ni][nj] = True
                heappush(pq, (arr[ni][nj], ni, nj, dist+1))




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    distance = [[int(1e99)] * N for _ in range(N)]

    result = dijkstra(0, 0)
    # print(f'#{tc} {result}')