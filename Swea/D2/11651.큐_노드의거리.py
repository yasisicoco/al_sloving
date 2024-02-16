def bfs(cur, G):
    # global visited
    # 큐 생성
    # 시작점 인큐
    # 인큐 표시
    # visited = [0] * (N + 1)
    q = []
    q.append(cur)
    visited[cur] = 1
    while q: # 처리 안된 정점이 남아있으면
        t = q.pop(0)
        if t == G: #처리한 정점이 도착노드와 같은 경우
            return visited[t] - 1 # 최단 경로 간선 수)
        for j in v[t]:
            if visited[j] == 0: #첫 방문인 경우
                q.append(j) # 큐에 추가
                visited[j] = visited[t]+1 #방문리스트 +1
    return 0  # G까지 경로가 없는경우


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접리스트
    v = [[] for _ in range(V+1)]
    # 방문리스트
    visited = [0] * (V+1)
    print(visited)

    for i in range(E):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G)}')