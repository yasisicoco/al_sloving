from collections import deque

def bfs(cur, goal):
    Q = deque()
    Q.append(cur) # 현재위치 넣기

    while Q:
        cur = Q.popleft()
        for i in v[cur]:
            if visited[i]:
                continue
            visited[i] = True
            ans[i] = ans[cur] + 1
            if i == goal:
                return ans
            Q.append(i)
    return -1

n = int(input()) # 전체 사람의 수 (정점)
p1, p2 = map(int, input().split()) # 비교해야 하는 두 사람
m = int(input()) # 부모 자식들간의 관계의 개수 (간선)

v = [[] for _ in range(n+1)] # 인접정점
visited = [False] * (n+1)
ans = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

# print(v)
visited[p1] = True
bfs(p1, p2)
if ans[p2] != 0:
    print(ans[p2])
else:
    print(-1)