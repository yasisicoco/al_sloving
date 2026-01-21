N, M = map(int, input().split())

def back():
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        back()
        arr.pop()
        

arr = []
back()