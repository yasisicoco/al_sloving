# import sys
# sys.stdin = open('12390.txt')

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

'''부분 집합의 합 1단계
N = len(arr)
bits = [0] * N
# 1. N자리 2진수 표현을 생성
def backtrack(k):
    if k == N:
        print(bits)
    else:
        bits[k] = 1
        backtrack(k + 1)

        bits[k] = 0
        backtrack(k + 1)

backtrack(0)
'''

'''부분 집합의 합 2단계
arr = [1, 2, 3]
N = len(arr)
bits = [0] * N
# 2. bits로 부터 원소를 가져와서 합과 원소수를 구하기
def backtrack(k):
    if k == N:
        print(bits, end=' ') # bits에는 하나의 부분집합
        S = cnt = 0
        for i in range(N):
            if bits[i] == 1:
                S += arr[i]
                cnt += 1
                print(arr[i], end=' ')
        print(',', S, cnt)
    else:
        bits[k] = 1
        backtrack(k + 1)

        bits[k] = 0
        backtrack(k + 1)

backtrack(0)
'''

'''부분 집합의 합 3단계
# 3. 지금까지 선택한 원소들의 합을 매개변수로 전달
# cur_sum: 0번 원소부터 k-1번 원소까지 선택한 원소들의 합
def backtrack(k, cur_sum, cur_cnt):
    if k == N:
        print(bits, end=' ') # bits에는 하나의 부분집합
        S = cnt = 0
        for i in range(N):
            if bits[i] == 1:
                S += arr[i]
                cnt += 1
                print(arr[i], end=' ')
        print(',', S, cur_sum, cnt, cur_cnt)
    else:
        bits[k] = 1     # arr[k]를 부분집합에 포함
        backtrack(k + 1, cur_sum + arr[k], cur_cnt + 1)

        bits[k] = 0     # arr[k]를 포함하지 않음
        backtrack(k + 1, cur_sum, cur_cnt)

backtrack(0, 0, 0)
'''

'''부분 집합의 합 3-1단계
M = K = 0  # M은 원소수, K는 목표합
arr = [1, 2, 3]
N = len(arr)
bits = [0] * N
# 3-1. 필요없는 코드 삭제
ans = 0
def backtrack(k, cur_sum, cur_cnt):
    global ans
    if k == N:
        if M == cur_cnt and K == cur_sum:
            ans += 1
    else:        
        backtrack(k + 1, cur_sum + arr[k], cur_cnt + 1)
        backtrack(k + 1, cur_sum, cur_cnt)

backtrack(0, 0, 0)
'''

'''부분 집합의 합 4단계
M = K = 0  # M은 원소수, K는 목표합
arr = [1, 2, 3]
N = len(arr)
bits = [0] * N
# 4. 가지 치기
ans = 0
def backtrack(k, cur_sum, cur_cnt):
    global ans
    if cur_sum > K or cur_cnt > M:
        return
    if k == N:
        if M == cur_cnt and K == cur_sum:
            ans += 1
        return
    else:
        backtrack(k + 1, cur_sum + arr[k], cur_cnt + 1)
        backtrack(k + 1, cur_sum, cur_cnt)

backtrack(0, 0, 0)
'''

'''풀이 1
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 12 + 1)]
    bits = [0] * 12
    # 4. 가지 치기
    ans = 0
    def backtrack(k, cur_sum, cur_cnt):
        global ans
        if cur_sum > K or cur_cnt > N:
            return
        if k == 12:
            if N == cur_cnt and K == cur_sum:
                ans += 1
            return
        else:
            backtrack(k + 1, cur_sum + arr[k], cur_cnt + 1)
            backtrack(k + 1, cur_sum, cur_cnt)
 
    backtrack(0, 0, 0)
    print(f'#{tc} {ans}')
'''

'''풀이2
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    def backtrack(k, cur_sum, cur_cnt):
        global ans
        if cur_sum > K or cur_cnt > N:
            return
        if k == 13:
            if N == cur_cnt and K == cur_sum:
                ans += 1
            return
        else:
            backtrack(k + 1, cur_sum + k, cur_cnt + 1)
            backtrack(k + 1, cur_sum, cur_cnt)
 
    backtrack(1, 0, 0)
    print(f'#{tc} {ans}')
'''