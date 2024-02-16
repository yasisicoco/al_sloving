def bfs(cur, N, G):
    D = [0] * (N + 1)
    R = [0] * (N + 1)
 
    visited = [0] * (N + 1)
    q = []
    q.append(cur)
    visited[cur] = 1

    # while q:
    #     t = q.pop(0)
    #     if t == G:
    #         return visited[t] - 1
    #     for j in v[t]:
    #         if visited[j] == 0:
    #             q.append(j)
    #             visited[j] = 1 # 방문확인용
    #             D[j] = D[t] + 1 # D는 얼마나왔는지 저장(거리)
    #             R[j] = R[t]   # R은 어디서왔는지 저장(장소)
    #             pass


# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     # 인접리스트
#     v = [[] for _ in range(V+1)]
#     # 방문리스트
#     # visited = [[0] for _ in range(V+1)]

#     for i in range(E):
#         a, b = map(int, input().split())
#         v[a].append(b)
#         v[b].append(a)
#     S, G = map(int, input().split())

#     print(f'#{tc} {}')