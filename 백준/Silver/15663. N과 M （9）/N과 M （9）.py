import sys
input = sys.stdin.readline

def recur():
    global result
    check = 0
    if len(num) == M:
        print(*num)
        return
    
    for i in range(N):
        if not vis[i] and check != lst[i]:
            vis[i] = True
            num.append(lst[i])
            check = lst[i]
            recur()
            num.pop()
            vis[i] = False
            
N, M = map(int, input().split())
lst = list(map(int, input().split()))
vis = [False] * N
num = []
lst.sort()            

recur()