N = int(input())
lst = list(map(int, input().split()))

def back():
    global result 

    if len(path) == N:
        total = 0
        for i in range(N-1):
            total += abs(path[i] - path[i+1])
        result = max(result, total)
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        path.append(lst[i])
        back()
        path.pop()
        visited[i] = False

visited = [False] * N
path = []
result = 0
back()
print(result)