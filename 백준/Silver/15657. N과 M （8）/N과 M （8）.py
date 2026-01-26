N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def back(s, arr):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(s, N):
        arr.append(lst[i])
        back(i, arr)
        arr.pop()

arr = []
back(0, arr)
