from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    lst = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        a, b = lst[i], lst[i+1]
        v[a].append(b)
        v[b].append(a)

    cnt = 0
    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = 1
            q = deque([j])
            while q:
                s = q.popleft()
                for e in v[s]:
                    if visited[e] == 1:
                        continue
                    visited[e] = 1
                    q.append(e)
            cnt += 1
    
    print(f'#{tc} {cnt}')