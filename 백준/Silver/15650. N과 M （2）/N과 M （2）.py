N, M = map(int, input().split())

def back():
    if len(arr) == M:
        temp = sorted(arr)
        if temp not in results:
            results.append(temp)
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        back()
        arr.pop()
        visited[i] = False
        

arr = []
visited = [False for _ in range(N+1)]
results = []
back()
for result in results:
    print(*result)