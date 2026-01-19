import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
arr = []

def back(N, M):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            back(N, M)
            arr.pop()
            visited[i] = False

back(N, M)