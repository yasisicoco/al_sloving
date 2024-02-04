import sys
sys.stdin = open('D2최빈수.txt')

T = int(input())
for _ in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    cnt = [0] * 101
    
    para = 0
    for score in scores:
        cnt[score] += 1
        if cnt[score] >= para:
            para = cnt[score] # 최빈수가 몇번 나왔는지
            result = score # 최빈수의 점수확인
    print(f'#{tc} {result}')