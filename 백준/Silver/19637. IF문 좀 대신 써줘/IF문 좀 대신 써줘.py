import sys
input = sys.stdin.readline

# 칭호, 캐릭수
N, M = map(int, input().split())

lst = []
for i in range(N):
    style, A = input().split()
    A = int(A)
    if lst and lst[-1] == A:
        continue
    lst.append([style, A])
    
for i in range(M):
    B = int(input())
    
    l = 0
    r = len(lst)
    while l <= r:
        mid = (l + r) // 2
        if B > lst[mid][1]:
            l = mid + 1
        else:
            r = mid - 1
    print(lst[r+1][0])