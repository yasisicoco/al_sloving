tc = int(input())
for tci in range(1, tc + 1):
    N = int(input())
    high = list(map(int, input().split()))
 
    max_high = 0 # 최대 낙차저장 초기화
    for i in range(N-1):
        cnt = 0 # 현재 상자의 낙차 초기화
        for j in range(i+1, N):
            if high[i] > high[j]:
                cnt += 1
        if max_high < cnt:
            max_high = cnt
    print(f'#{tci} {max_high}')