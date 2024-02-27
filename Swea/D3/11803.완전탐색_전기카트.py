def find_(i, j, sumone):
    global result

    # 기저함수: 구역을 다 돌았을 때
    if i == N-1: # 행을 다 돌았다면
        if sumone+arr[j][0] <= result:
            result = sumone+arr[j][0]
            return
    
    if sumone >= result:
        return

    for c in range(1, N): # 1부터 N-1번째까지 행 구역 순회
        if visited[c]:
            continue

        visited[c] = True
        find_(i+1, c, sumone+arr[j][c]) # 0, 0 부터 더하기
        visited[c] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    
    # 방문처리
    visited = [False for _ in range(N)]

    result = 999999999999999
    find_(0, 0, 0) # 0, 0 좌표에서 최솨값을 더할 0을 갖고 시작
    print(f'#{tc} {result}')