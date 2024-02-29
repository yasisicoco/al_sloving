T = int(input())
for tc in range(1, T+1):
    # N = 배열의 크기, M = 정사각 영역의 수
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 정사각영역의 좌상단 위치와 변의 길이
    result = 0
    for _ in range(M):
        a, b, K = map(int, input().split())
        
        sumone = 0
        for i in range(N):
            for j in range(N):
                if a <= i < a + K and b <= j < b + K:
                    sumone += arr[i][j] # 합산 처리
                    arr[i][j] = 0 # 들렸던 곳은 0 처리
        result += sumone
    
    print(f'#{tc} {result}')        