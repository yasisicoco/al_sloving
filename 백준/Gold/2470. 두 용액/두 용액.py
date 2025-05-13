import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 포인터
start = 0
end = n-1

# 저장 인덱스값
s = start
e = end
pointZero = float('inf')

while start < end:
    result = arr[start] + arr[end]

    if abs(result) <= pointZero:
        pointZero = abs(result)
        s, e = start, end
        if result == 0:
            break

    if result < 0:
        start += 1
    else:
        end -= 1

print(arr[s],arr[e])