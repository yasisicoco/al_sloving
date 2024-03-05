di = [0, 1]
dj = [1, 0]

def temp(si, sj):
    global result
    for k in range(2): # 방향
        leng = 1 # 초기화 (들어왔을때 1)
        for l in range(1, 101): # 길이
            ni = si + di[k] * l
            nj = sj + dj[k] * l
            
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1: # 다음지역이 1인 경우
                leng += 1 # 길이 + 1
            else:
                break
            
        # 길이만큼 다 돌고 최대길이 비교
        if result <= leng:
            result = leng

T = int(input())    
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 완탐 시작지점부터 끝까지 순회
    result = 0 # 가장 긴 구조물의 길이
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: # 만약 1이면 길이확인 시작
                temp(i, j) # 완탐이니까 오른쪽, 아래만 확인
    
    print(f'#{tc} {result}')