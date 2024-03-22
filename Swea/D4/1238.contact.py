import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(S):
    q = deque()
    q.append(S)
    visited = [0] * (101)
    visited[S] = 1

    max_number = S
    max_depth = 1

    while q:
        cur = q.popleft()

        for i in v[cur]:
            if visited[i]:
                continue
            visited[i] = 1 + visited[cur]

            if max_depth < visited[i] or (max_depth == visited[i] and max_number < i):
                max_depth = visited[i]
                max_number = i
            q.append(i)
    
    return max_number

T = 10
for tc in range(1, T+1):
    V, S = map(int, input().split())
    arr = list(map(int, input().split()))

    v = [[] for _ in range(101)] # 인접리스트

    for i in range(0, V, 2):
        s, e = arr[i], arr[i+1]
        v[s].append(e)
    
    print(f'#{tc} {bfs(S)}')