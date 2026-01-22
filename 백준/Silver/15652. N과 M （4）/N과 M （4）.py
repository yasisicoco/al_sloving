N, M = map(int, input().split())

def back(start):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(start, N+1):
        arr.append(i)
        back(i)
        arr.pop()
        
arr = []
back(1)
