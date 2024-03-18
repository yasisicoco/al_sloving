def quick(lo, hi):
    if lo >= hi:
        return 
    
    i, j = lo, hi
    p = arr[lo]
    while i <= j:
        while i <= hi and p >= arr[i]:
            i += 1
        while p < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[lo], arr[j] = arr[j], arr[lo]
    quick(lo, j-1)
    quick(j+1, hi)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    quick(0, len(arr)-1)
    print(f'#{tc}', arr[N//2])
