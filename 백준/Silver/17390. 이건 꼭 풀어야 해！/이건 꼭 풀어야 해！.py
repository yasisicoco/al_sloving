import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = sorted(map(int, input().split()))

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + arr[i-1]
# print(dp)
    
for i in range(Q):
    L, R = map(int, input().split())
    print(dp[R]-dp[L-1])