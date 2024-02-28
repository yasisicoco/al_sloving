# D3 탐욕_컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    

    contain = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    truck.sort(reverse=True)
    contain.sort(reverse=True)
    # print(contain, truck)

    sumone = 0 # 총 이동 무게
    for i in range(M): # 트럭
        result = 0 # 각 트럭
        for j in range(N): # 컨테이너
            if truck[i] >= contain[j] and result < contain[j]: # 컨테이너 무게가 적재량보단 작고, 다른 컨테이너보단 크다면
                result = contain[j]
                contain[j] = 0
        sumone += result # 더하고 초기화.
    
    print(f'#{tc} {sumone}')