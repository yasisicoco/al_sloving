tc = int(input()) # 테스트 케이스 처음만 입력
for tctc in range(1, tc + 1): # 테스트케이스만큼 순환
    N = int(input()) # 양수의 개수 N
    ai = list(map(int, input().split())) # N개의 양수 ai
    min_val = ai[0] # 최대 최소 초기화
    max_val = ai[0]
    for i in ai: # lst 를 돌며 min max 판별
        if min_val > i:
            min_val = i
        if max_val < i:
            max_val = i
        result = max_val - min_val
    print(f'#{tctc} {result}')