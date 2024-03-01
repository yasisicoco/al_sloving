T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(N-1): # 버블정렬
        for j in range(i+1, N):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[i] # 자리바꾸기
    cnt = 0
    for i in range(N):
        if 0 <= i < N:
            if lst[i-1] == lst[i]: # 이전 인덱스 값과 같다면
                continue
            else:
                cnt += 1 # 아니면 +1
            if cnt == K: # cnt가 K가 되었을 때
                print(f'#{tc} {lst[i]}')
                break