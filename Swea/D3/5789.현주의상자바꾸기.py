T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N # N개의 상자리스트
    for i in range(1, Q+1): # Q번 반복 Q는 1부터
        L, R = map(int, input().split())
        L -= 1 
        rng = R-L+1 # L부터 R까지의 갯수를
        for _ in range(rng): # 반복
            if L < R: # L이 R보다 작을동안
                arr[L] = i # arr의 L번째에 i입력
                L += 1 # L에 +1 해서 반복, arr[R]전까지
    print(f'#{tc}', *arr)