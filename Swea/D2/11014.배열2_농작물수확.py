T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 9999999999999999
    for r in range(1, N):
        for c in range(1, N):
                        
            # 오른쪽 부분
            sum_right = 0
            for i in range(N): # 맨위부터 맨아래까지
                for j in range(c, N): # 오른쪽 c부터 N까지
                    sum_right += arr[i][j]
            
            # 왼쪽 위 부분
            sum_lefttop = 0
            for i in range(N-r): # 0부터 N-r 까지
                for j in range(c): # 0부터 c까지
                    sum_lefttop += arr[i][j]
            
            # 왼쪽 아래 부분
            sum_leftbot = 0
            for i in range(N-r, N): # N-r 부터 N까지
                for j in range(c):
                    sum_leftbot += arr[i][j]
            
            # 다돌고 최대값과 최소값을 구해서
            max_val = max(sum_right, sum_lefttop, sum_leftbot)
            min_val = min(sum_right, sum_lefttop, sum_leftbot)
            if result >= max_val - min_val: # 차이가 작다면
                result = max_val - min_val # 결과값 갱신
    
    print(f'#{tc} {result}')