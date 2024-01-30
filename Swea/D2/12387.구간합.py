T = int(input())
for tc in range(1, T + 1):
    max_sum = 0
    min_sum = 1000000
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    for s in range(0, N - M + 1):
        sum = 0
        for i in range(s, s + M):
            sum += ai[i]
 
        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum
 
    print(f'#{tc} {max_sum - min_sum}')
