N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def back(s):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(s, N+1):
        arr.append(lst[i-1])
        back(s)
        arr.pop()
        
arr = []
back(1)