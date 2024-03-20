# 절단기의 높이는 나무의 높이 이하

def cutting(lo, hi):
    global result
    
    if lo > hi:
        return
    
    mid = (lo + hi) // 2
    
    if result >= mid:
        return
    
    sumone = 0
    for i in range(N):
        if lst[i] > mid:
            sumone += lst[i] - mid
    
    if sumone >= M: # 나무의 높이의 합보다 크다면 중간값이 작다는 뜻
        result = max(result, mid) # 자른 높이가 높을수록(mid값이 클수록) 환경을 보호함
        cutting(mid+1, hi)
    else:
        cutting(lo, mid-1)

N, M = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)

result = 0
cutting(0, max(lst))
print(result)