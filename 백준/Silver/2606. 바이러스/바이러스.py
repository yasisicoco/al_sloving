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




# state 2 (진화한 나)
# import sys
# sys.setrecursionlimit(10 ** 6)

# def dfs(cur):
    # global cnt
    # for i in v[cur]:
        # if visited[i] == True:
            # continue
        # visited[i] = True
        # cur = i
        # cnt += 1
        # dfs(cur)

# V = int(input())
# E = int(input())

# v = [[] for _ in range(V+1)]
# visited =[False for _ in range(V+1)]

# cnt = 0
# for i in range(E):
    # a, b = map(int, input().split())
    # v[a].append(b)
    # v[b].append(a)

# visited[1] = True
# dfs(1)
# print(cnt)