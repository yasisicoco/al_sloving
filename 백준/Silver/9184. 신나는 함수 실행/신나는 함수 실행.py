import sys
input = sys.stdin.readline

def dfs(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dfs(20, 20, 20)
    
    if a < b and b < c:
        dp[a][b][c] = dfs(a, b, c-1) + dfs(a, b-1, c-1) - dfs(a, b-1, c)
    else:
        dp[a][b][c] = dfs(a-1, b, c) + dfs(a-1, b-1, c) + dfs(a-1, b, c-1) - dfs(a-1, b-1, c-1)

    return dp[a][b][c]

dp = [[[None for _ in range(101)] for _ in range(101)] for _ in range(101)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    result = dfs(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')
