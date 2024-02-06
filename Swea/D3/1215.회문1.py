import sys
sys.stdin = open('D3회문1.txt')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 회문의 길이 4
    arr = [list(input()) for _ in range(8)] # 글자 판
    # for line in arr:
    #     print(*line)

    cnt = 0
    # 세로회문검사
    for i in range(8): 
        for j in range(8-N+1):
            e = j+N-1 # 세로회문 마지막 str
            for k in range(N//2): # 길이의 반만큼 실행
                if arr[j+k][i] != arr[e-k][i]:
                    break
            else:
                cnt += 1

    # 가로회문검사
    for i in range(8):
        for j in range(8-N+1):
            e = j+N-1
            for k in range(N//2):
                if arr[i][j+k] != arr[i][e-k]:
                    break
            else:
                cnt += 1
    print(f'#{tc} {cnt}')