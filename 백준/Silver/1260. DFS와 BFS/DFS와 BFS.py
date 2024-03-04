from collections import deque

def dfs(cur):
    global dfs_check
    
    for i in v[cur]:
        if visited[i]: # True
            continue
        visited[i] = True # if False > True
        if i not in dfs_check:
            dfs_check.append(i) 
        cur = i
        dfs(cur)

def bfs(cur):
    global bfs_check

    Q = deque()
    Q.append(v[cur])

    while Q:
        cur = Q.popleft()
        for i in cur:
            if visited[i]:
                continue
            visited[i] = True
            if i not in bfs_check:
                bfs_check.append(i)
            Q.append(v[i])



# func()------------------------------------------
    
N, M, V = map(int, input().split())

# 인접정점
v = [[] for _ in range(N+1)] 
# 방문확인
visited = [False] * (N+1)

# 간선수만큼 반복
for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a) 

for vv in v:
    vv.sort()

dfs_check = [V]
visited[V] = True
dfs(V)
print(*dfs_check)

# BFS---------------------------------------------
bfs_check = [V]
# 방문확인 초기화
visited = [False] * (N+1)
visited[V] = True
bfs(V)
print(*bfs_check)