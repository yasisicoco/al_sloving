from heapq import heappush, heappop

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    v = [[] for _ in range(N+1)] # 인접리스트
    dist = [0xffff] * (N+1) # 누적 거리

    for _ in range(E):
        s, e, w = map(int, input().split())
        v[s].append([w, e])
    
    def dijkstra(start):
        pq = []
        heappush(pq, (0, start))

        while pq:
            w, cur = heappop(pq)

            for to in v[cur]:
                nd = to[0]
                nn = to[1]

                new_d = nd + w
                if new_d >= dist[nn]:
                    continue
                dist[nn] = new_d
                heappush(pq, (new_d, nn))
                
        return dist[N]

    result = dijkstra(0)
    print(f'#{tc} {result}')