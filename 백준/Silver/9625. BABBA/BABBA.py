K = int(input())
dp = [0] * (K+2)
dp[0] = 1
dp[1] = 0

for i in range(2, K+2):
    dp[i] = dp[i-1] + dp[i-2]

print(f'{dp[K]} {dp[K+1]}')