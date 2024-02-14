import sys
sys.stdin = open('12390.txt')

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
    print(f'{tc} {ans}')