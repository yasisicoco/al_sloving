import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M, R = map(int, input().split()) # 정점, 간선, 시작정점

# 인접 리스트
v = [[] for _ in range(N+1)]
# 방문처리 리스트
visited = [False for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

for j in v:
    j.sort(reverse=True)

depth = [-1 for _ in range(N+1)] # 방문안한 정점은 -1

def dfs(cur, dep):
    for i in v[cur]:
        if visited[i]: # True
            continue
        visited[i] = True
        depth[i] = dep
        dfs(i, dep + 1)

visited[R] = True # R은 시작정점
depth[R] = 0 # 시작정점 R의 깊이는 0
dfs(R, 1)
for k in range(1, N+1):
    print(depth[k])