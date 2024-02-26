import sys
sys.stdin = open('pangpang.txt')

di = [0, 1, 0, -1] # 오 아래 왼 위
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # for line in arr:
        # print(*line)
    
    max = 0 # 더하기값과 비교할 최댓값
    for i in range(N):
        for j in range(M):
            cnt = 0 # 시작점에서 더하기값 초기화
            num = arr[i][j]
            for spin in range(1, num+1): # 시작점 값만큼 범위증가 
                for k in range(4): # 상하좌우 돌면서 더하기
                    dr = i + di[k] * spin
                    dc = j + dj[k] * spin
                    if 0 <= dr < N and 0 <= dc < M:
                        cnt += arr[dr][dc]
            if max < cnt+num:
                max = cnt+num
            dr = 0
            dc = 0
    print(f'#{tc} {max}')    
    
    
    
#state 2
di = [0, -1, 1, 0]
dj = [1, 0, 0, -1]

def vec(i, j):
    global num, result
    
    ans = arr[i][j]
    for l in range(1, num+1):
        for k in range(4):
            ni = i + di[k] * l
            nj = j + dj[k] * l
            
            if 0 <= ni < N and 0 <= nj < M: # 위아래양옆
                ans += arr[ni][nj]
                if result <= ans:
                    result = ans
                

T = int(input())    
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = -1
    for i in range(N):
        for j in range(M):
            num = arr[i][j] # 터지는 풍선 안에 든 꽃가루 갯수
            vec(i, j)
    print(f'#{tc} {result}')