N, M = map(int, input().split())
lst = list(map(int, input().split()))

def back(s):
    check = 0
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(s, N):
        if check != lst[i]:
            check = lst[i]
            arr.append(lst[i])
            back(i)
            arr.pop()

lst.sort()
arr = []
back(0)