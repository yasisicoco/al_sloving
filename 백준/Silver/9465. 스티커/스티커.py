T = int(input())
for tc in range(T):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]

    # 예외처리
    if n == 1:
        print(max(score[0][0], score[1][0]))
        continue
    
    # DP 배열
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = score[0][0]
    dp[1][0] = score[1][0]
    # 길이 2
    dp[0][1] = score[1][0] + score[0][1]
    dp[1][1] = score[0][0] + score[1][1]
    # 길이 > 2
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + score[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + score[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))