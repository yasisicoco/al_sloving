import sys
input = sys.stdin.readline
V = int(input())
E = int(input())

# 인접리스트
v = [[] for _ in range(V+1)]
# 방문확인리스트
visited = [False for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

# print(v)

def dfs(cur):
    for j in v[cur]:
        if visited[j]:
            continue
        visited[j] = True
        cur = j
        dfs(cur)

visited[1] = True
dfs(1)
# print(visited)

cnt = 0
for k in range(V+1):
    if visited[k] == True:
        cnt += 1

print(cnt-1)