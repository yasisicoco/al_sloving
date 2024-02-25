from sys import stdin; input = stdin.readline

def virus(start, vertex):
    visited = [0] * (vertex + 1)
    stack = []
    visited[start] = 1
    # print(start)
    cnt = 0
    while True:
        for a in adjl[start]:
            if visited[a] == 0:
                visited[a] = 1
                stack.append(start)
                start = a
                # print(start)
                cnt += 1
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
                # return cnt
    return cnt

# V : 컴퓨터 수(노드 수)
V = int(input())
# E : 연결 쌍 수(간선 수)
E = int(input())
# 인접 리스트
adjl = [[] for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u)   # 무향그래프

<<<<<<< HEAD
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
=======
print(virus(1, V))
>>>>>>> ccd870cb342da1db3745d2b59d4b49be76609fee
