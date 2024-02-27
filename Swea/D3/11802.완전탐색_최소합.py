# 11802. 완전검색_최소합
# state 1

def find_(i, j, min_val):
    global result
    
    if i == N-1 and j == N-1: # 좌표값이 배열의 마지막일때
        if min_val <= result: # 최소값이라면?
            result = min_val  # 바꿔주자
        return
    
    # 오른쪽(i, j+1) 으로
    if j + 1 < N:
        find_(i, j+1, min_val+arr[i][j+1]) #이동할 좌표값 더하면서 그곳의 값도 더해줌

    # 아래(i+1, j) 로
    if i + 1 < N:
        find_(i+1, j, min_val+arr[i+1][j]) #이동할 좌표값 더하면서 그곳의 값도 더해줌


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[False] * N for _ in range(N)]

    result = 99999
    start_val = arr[0][0] # 출발지 값
    find_(0, 0, start_val)
    print(f'#{tc} {result}')