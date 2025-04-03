from collections import deque

def bfs(N, K):
    MAX = 100001
    visited = [False] * MAX
    time = [0] * MAX
    prev = [-1] * MAX 

    q = deque()
    q.append(N)
    visited[N] = True

    while q:
        cur = q.popleft()

        if cur == K:
            # 경로 복원
            path = []
            while cur != -1:
                path.append(cur)
                cur = prev[cur]
            path.reverse()
            return time[K], path

        for next in [cur - 1, cur + 1, cur * 2]:
            if 0 <= next < MAX and not visited[next]:
                visited[next] = True
                time[next] = time[cur] + 1
                prev[next] = cur 
                q.append(next)


N, K = map(int, input().split())
result_time, result_path = bfs(N, K)

print(result_time)
print(" ".join(map(str, result_path)))
