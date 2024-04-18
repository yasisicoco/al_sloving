# 함수를 만들고 각각 정의해준다.
# 그리고 리턴값으로 다시 그 함수를 받는다.
# A - B - BA - BAB - BABBA - BABBABAB - BABBABABBABBA
# BABBABABBABBABABBABAB - BABBABABBABBABABBABABBABBABABBABBA
#        0   1    2   3   4   5   6   7   8   9    10 
# 규칙 A: 1 - 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34
# 규칙 B: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55

K = int(input())
dp = [0] * (K+1)
dp[0] = [1, 0]

for cnt in range(1, K+1):
    dp[cnt] = dp[cnt-1][1], dp[cnt-1][0] + dp[cnt-1][1]

print(*dp[K])