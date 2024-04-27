#계단의 갯수
n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
    
dp = [0] * (n+1)
# 1번 계단
dp[1] = stairs[1]
if n == 1:
    print(dp[1])
    exit()
# 2번 계단까지 갔을떄
dp[2] = stairs[1] + stairs[2]
if n == 2:
    print(dp[2])
    exit()
# 3번 계단부터-
for i in range(3, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1], dp[i-2]) + stairs[i]
print(dp[n])