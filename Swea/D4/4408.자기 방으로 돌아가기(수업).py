# 4408. 자기 방으로 돌아가기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 복도 리스트 초기화
    corridor = [0] * 400
    max_v = 0

    for _ in range(N):
        # 현재방 s, 돌아갈 방 e
        s, e = map(int, input().split())

        # 특징 2번 아랫방을 윗방으로 변경
        if s % 2 == 0: s -= 1
        if e % 2 == 0: e -= 1

        # 특징 1번 출발지보다 목적지가 더 큰 값이 되도록 swap
        if s > e: s, e = e, s # swap

        for i in range(s, e + 1):
            corridor[i] += 1
            max_v = max(corridor[i], max_v)
    print(f'#{tc} {max_v}')
    
    
# state 2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    path = [0] * 400 # 통로
    
    for i in range(N):
        s, e = map(int, input().split())
        
        if s > e:
            s, e = e, s
        
        # 한줄의 방 배열로 압축
        if s % 2 == 0:
            s -= 1
        if e % 2 == 0:
            e -= 1
            
        for j in range(s, e+1):
            path[j] += 1
        
        max_val = max(path)
    print(f'#{tc} {max_val}')