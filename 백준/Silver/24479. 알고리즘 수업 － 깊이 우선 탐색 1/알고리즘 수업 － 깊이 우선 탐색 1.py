import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M, R = map(int, input().split())
    
# 인접리스트
v = [[] for _ in range(N+1)]
# 방문 처리 리스트
visited = [False for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
    
for j in v:
    j.sort()
    
vis = [0 for _ in range(N+1)] # 0 / 1 2
cnt = 1
def dfs(cur):
    global cnt
    
    for i in v[cur]:
        if visited[i] == True:
            continue
        visited[i] = True
        cur = i
        cnt += 1
        vis[i] = cnt
        dfs(cur)
        # 여기로 돌아온다. i will be back
        
vis[R] = 1
visited[R] = True
dfs(R)

for k in range(1, N+1):
    print(vis[k])