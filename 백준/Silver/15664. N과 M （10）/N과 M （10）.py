N, M = map(int, input().split())
lst = list(map(int, input().split()))

def back(s):
    check = 0
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(s, N):
        if not visited[i] and check != lst[i]:
            check = lst[i]
            visited[i] = True
            arr.append(lst[i])
            back(i+1)
            arr.pop()
            visited[i] = False

lst.sort()
arr = []
visited = [False] * (N+1)
back(0)
# 1 7 9 9 