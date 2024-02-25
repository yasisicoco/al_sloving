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