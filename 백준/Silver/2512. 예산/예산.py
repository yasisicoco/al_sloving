import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = int(input())

if sum(lst) <= M:
    print(lst[-1])
else:
    s, e = 0, lst[-1]
    result = 0
    while s <= e:
        mid = (s+e) // 2
        temp = 0
        for i in range(N):
            if lst[i] < mid:
                temp += lst[i]
            else:
                temp += mid
        
        if temp <= M:
            s = mid + 1
            result = mid
        else:
            e = mid - 1
    print(result)