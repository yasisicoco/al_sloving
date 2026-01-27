N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def back():
    check = 0
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(N):
        if not visited[i] and check != lst[i]:
            check = lst[i]

            visited[i] = True
            arr.append(lst[i])
            back()
            arr.pop()
            visited[i] = False

visited = [False] * (N+1)
arr = []
back()
