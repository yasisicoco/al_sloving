import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * 100001
left = 0
ans = 0

for right in range(n):
    count[arr[right]] += 1

    while count[arr[right]] > k:
        count[arr[left]] -= 1
        left += 1
    ans = max(ans, right - left + 1)

print(ans)