import sys
# sys.stdin = open('swea\\input\\11315.txt')
sys.stdin = open('al_sloving\\swea\\input\\11315.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    result = 'NO'
    if result == 'NO':
        for i in range(N): # 세로
            for q in range(N):
                if arr[i][q] == 'o':
                    continue
                else:
                    break
            result = 'YES'

    elif result == 'NO':        
        for j in range(N): # 가로
            for w in range(N):
                if arr[w][j] == 'o':
                    continue
                else:
                    break
            result = 'YES'
    
    elif result == 'NO': # 대각선
        for k in range(N):
            if arr[k][k] == 'o':
                continue
            else:
                break
        result = 'YES'

    elif result == 'NO': # 역대각선
        for l in range(N):
            if arr[N-1-l][l] == 'o':
                continue
            else:
                break
        result = 'YES'

    print(f'#{tc} {result}')