N = int(input())

# dp초기화
dp = [[-1] * 10 for _ in range(N)]

# n = 1일 때, 값 넣어주기
for j in range(10):
    dp[0][j] = 1

for i in range(1, N):
    prev = [-1] * 10
    for j in range(10):
        if j == 0:
            prev[j] = dp[i-1][j+1]
        elif j == 9:
            prev[j] = dp[i-1][j-1]
        else:
            prev[j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    for j in range(10):
        dp[i][j] = prev[j]

result = sum(dp[N-1][1:10]) % 1000000000
print(result)