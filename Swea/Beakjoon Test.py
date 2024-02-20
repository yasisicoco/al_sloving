V, E = map(int, input().split())


visited[cur] = 1
def recur(cur):
    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        cur = i
        # 연산 넣기

        recur(cur)

# 인접리스트
v = [[] for _ in range(V+1)]
# 방문확인 리스트
visited = [False for _ in range(V+1)]
visited2 = [[0] for _ in range(V+1)]


for i in range(E):
    a, b = map(int, input().split())
    v[a].append[b]
    v[b].append[a]
    
recur(cur)

