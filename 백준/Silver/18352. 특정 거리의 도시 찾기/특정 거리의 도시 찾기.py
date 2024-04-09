from collections import deque
import sys
input = sys.stdin.readline

def bfs():

    q = deque()
    q.append(X)
    visited[X] = 1

    while q:
        cur = q.popleft()
        if visited[cur] == K+1:
            lst.append(cur)
        
        if visited[cur] > K+1:
            break

        for i in v[cur]:
            if visited[i] == 0:
                visited[i] = visited[cur] + 1
                q.append(i)


# 도시개수 N, 도로개수 M, 거리정보 K, 출발도시 X
N, M, K, X = map(int, input().split())
v = [[] for _ in range(N+1)]
visited = [ 0 for _ in range(N+1)]

for i in range(M): # 도로개수M
    a, b = map(int, input().split())
    v[a].append(b) # 단방향


lst = []
bfs()
lst.sort()
if lst:
    for line in lst:
        print(line)
else:
    print(-1)