def back(i, M, s, K):
 
    global ans
 
    if s == K:
        ss = []
        for j in range(M):
            if bits[j] == 1:
                ss.append(L[j])
        if len(ss) == N:
            ans += 1
     
    elif s > K: # 최대값보다 부분집합값합이 더 큰 경우
        return
    elif i == M: # 끝까지 돈 경우
        return
    else:
        bits[i] = 1
        back(i+1, M, s+L[i], K)
        bits[i] = 0
        back(i+1, M, s, K)
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = list(range(1, 13))
    M = len(L)
    bits = [0] * M
    ans = 0
 
    back(0, M, 0, K)
    print(f'#{tc} {ans}')
    
    
    
# 변영인강사님 강의
A = [3, 1, 2, 5, 4]  # 부분집합을 만들 원래 자연수들의 집합
subset = [0] * len(A)  # 부분집합을 표시할 리스트
results = []  # 조건을 만족하는 부분집합을 저장할 리스트

def f(i, N, s, t):  # i -> 몇 번째의 원소를 넣을지뺄지 결정
    # N -> 전체 원소의 개수
    # s -> 현재까지의 부분집합 합 sum
    # t -> 목표로하는 target 값
    if s == t:  # 현재까지의 합과 찾으려는 합이 일치한다면
        tmp = []
        for j in range(i):
            if subset[j]:
                tmp.append(A[j])
        results.append(tmp)  # 여기서 로직이 끝남
    elif i == N:  # 모든 원소에 대한 탐색이 끝났다면
        return
    elif s > t:  # 지금까지의 합이 목표보다 크다면
        return # 남은 원소를 고려할 필요 X
    else: # 아직 남은 원소가 있고, s도 t보다 작아서...
        subset[i] = 1  # True
        f(i + 1, N, s + A[i], t)  # i 뎁스의 원소를 포함
        subset[i] = 0  # 부분집합에서 현재 i 깊이를 제거하고
        f(i + 1, N, s, t)

f(0, len(A), 0, 6)  # 목표하는 부분집합의 합이 6일 때
print(*results, sep='\n')