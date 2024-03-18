def binary(l, r, num, vec):
    global cnt
    m = (l+r) // 2

    if num == A[m]:
        cnt += 1
        return
    if l == r:
        return

    if B[m] >= num: # 미드값이 키값보다 클때
        if vec == 2:
            binary(l, m-1, num, 1)
    else:
        if vec == 1:
            binary(m+1, r, num, 2)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    cnt = 0
    for i in range(M):
        binary(0, len(B)-1, B[i])
        print(f'#{tc}')