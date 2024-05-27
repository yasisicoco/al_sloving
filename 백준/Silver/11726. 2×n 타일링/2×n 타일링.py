n = int(input())
dp = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        dp[1] = 1
        continue
    elif i == 2:
        dp[2] = 2
        continue
    
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)