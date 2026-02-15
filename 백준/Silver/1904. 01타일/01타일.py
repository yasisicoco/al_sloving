import sys
input = sys.stdin.readline

N = int(input())

# N=1일 때는 1, 1개
# N=2일 때는 00 11, 2개
# N=3일 때는 001, 100, 111, 3개
# N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열
# N=5일 때는 00111, 10011, 11001, 11100, 00001, 00100, 10000, 11111 등 총 8개

if N == 1:
    print(1)
else:
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    # print(dp)
    print(dp[N])