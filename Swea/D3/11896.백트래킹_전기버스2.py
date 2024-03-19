# 최소한의 교체횟수
# 출발지는 카운트X
# 종점에는 배터리X

def stop(cur, cnt):
    global result
    
    if cur >= N-1:
        if result > cnt-1:
            result = cnt-1
        return
    
    if result <= cnt-1:
        return

    for i in range(M[cur], 0, -1):
        stop(cur+i, cnt+1) # 충전, 카운트 + 1

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]    
    M = lst[1:]

    result = N
    stop(0, 0)
    print(f'#{tc} {result}')