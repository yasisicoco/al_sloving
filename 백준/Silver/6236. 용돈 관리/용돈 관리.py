import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
min_val = max(arr)
max_val = sum(arr)

while min_val <= max_val:
    mid = (min_val + max_val) // 2
    tmp = mid
    cnt = 1
    for i in arr:
        if tmp - i < 0:
            tmp = mid
            cnt += 1
        tmp -= i
    
    if cnt > m:
        min_val = mid + 1
    else:
        max_val = mid - 1
        ans = mid

print(ans)