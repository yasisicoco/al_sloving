import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n-1
near_zero = 2000000000

s = start
e = end

while start < end:
    result = arr[start] + arr[end]

    if abs(result) <= near_zero:
        near_zero = abs(result)
        s, e = start, end
        if result == 0:
            break
    
    if result < 0:
        start += 1

    else: 
        end -= 1

print(arr[s], arr[e])        