N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtrack():
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        path.append(arr[i-1])
        backtrack()
        visited[i] = False
        path.pop()

visited = [False] * (N + 1)
path = []
backtrack()