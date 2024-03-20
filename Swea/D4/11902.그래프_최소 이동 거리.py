T = int(input())
for tc in range(1, T+1):
    # 마지막 연결지점 번호 N, 도로의 개수 E
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(E):
        # 정점1, 정점2, 가중치
        s, e, w = map(int, input().split())
        G[s].append((e, w))
    
    D = [0xfffff] * (N+1) # 출발점에서 각 정점까지 최단 거리
    # P = [i for i in range(V+1)] # 최단 경로 트리
    D[0] = 0 
    Q = [0] # 출발점 삽입

    while Q:
        s = Q.pop(0)
        # 출발점 --> u --> v 로 가는 경로를 확인
        # u의 인접 정점(v) 에 대해 작업 => (u, v) 간선 완화 작업
        for e, w in G[s]:
            if D[e] > D[s] + w:
                D[e] = D[s] + w
                Q.append(e)
    
    print(f'#{tc} {D[N]}')