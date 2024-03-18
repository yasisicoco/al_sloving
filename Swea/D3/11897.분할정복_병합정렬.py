from collections import deque

def sort_merge(lst):
    global cnt

    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    l = sort_merge(lst[:mid])
    r = sort_merge(lst[mid:])
    
    
    if l[-1] > r[-1]:
        cnt += 1

    l = deque(l)
    r = deque(r)
    result = []
    while l and r:
        if l[0] < r[0]:
            result.append(l.popleft())
        else:
            result.append(r.popleft())

    result.extend(l)
    result.extend(r)
    return result

T = int(input())    
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = sort_merge(arr)
    
    print(f'#{tc}', ans[N//2], cnt)