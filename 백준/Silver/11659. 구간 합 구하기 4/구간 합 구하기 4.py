import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i]= arr[i-1] + dp[i-1]
    
for i in range(M):
    i, j = map(int, input().split())
    result = dp[j] - dp[i-1]
    print(result)