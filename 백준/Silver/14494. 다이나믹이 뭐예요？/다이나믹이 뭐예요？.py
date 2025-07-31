import sys
input = sys.stdin.readline

n, m = map(int, input().split())
D = [[0] * (m+2) for _ in range(n+2)]
D[1][1] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            continue
        D[i][j] = D[i-1][j] + D[i][j-1] + D[i-1][j-1]

print(D[n][m] % 1000000007)