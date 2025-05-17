import sys
input  = sys.stdin.readline

n, k = map(int, input().split())

pack = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    # 무게, 가치
    weight = pack[i-1][0]
    value = pack[i-1][1]
    for w in range(k+1):
        if weight > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

print(dp[n][k])