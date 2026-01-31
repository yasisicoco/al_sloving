N = int(input())
lst = [i+1 for i in range(N)]

def back():
    if len(result) == N:
        print(*result)

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        result.append(i)
        back()
        result.pop()
        visited[i] = False

result = []
visited = [False] * (N+1)
back()
