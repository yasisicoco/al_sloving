import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
    visited[cur] = True
    
    q = deque()
    q.append(cur)
        
    while q:
        cur = q.popleft()
        
        for k in range(1, 7): # 주사위 1~6
            next_cur = cur + k

            if 0 < next_cur <= 100 and not visited[next_cur]:
                if arr[next_cur]:
                    next_cur = arr[next_cur][0]
                if not visited[next_cur]:
                    q.append(next_cur)
                    visited[next_cur] = True
                    cnt[next_cur] = cnt[cur] + 1
                
# N개의 줄, M개의 뱀
N, M = map(int, input().split())
cnt = [0] * 101
visited = [False] * 101

# 사다리타기
arr = [[] for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    arr[x].append(y)
# 뱀따라가기
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)

bfs(1)
print(cnt[100])