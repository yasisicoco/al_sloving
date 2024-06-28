N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(K):
    ans += arr[i]

result = ans

for i in range(K, N):
    ans += arr[i] - arr[i-K]
    result = max(ans, result)

print(result)