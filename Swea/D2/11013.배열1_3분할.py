# 구간을 세개로 나눔
# 나눈 세구간에서 각각 더함
# 더한 값 중에서 최대값과 최소값을 구함
# 최대값과 최소값의 차이가 최소인 경우를 찾아 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    min_val = 999999999
    for i in range(1, N-1): # 정수 N개를 3구간으로 나누는 법
        for j in range(i+1, N):
            one = sum(lst[:i])
            two = sum(lst[i:j])
            thr = sum(lst[j:])
            result = max(one, two, thr) - min(one, two, thr)
            if min_val >= result:
                min_val = result
    print(f'#{tc} {min_val}')