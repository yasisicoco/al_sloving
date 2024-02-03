# 1979. 어디에 단어가 들어갈 수 있을까?
# import sys
# sys.stdin = open('whereword.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) + [0] for _ in range(N)]+[[0]*(N+1)]
#     N += 1
#     # 가로, 세로로 연속한 1의 개수가 K인 경우이 수
#     ans = 0
#     for j in range(N):
#         cnt = 0 # j열에서 연속한 1의 개수
#         for i in range(N):
#             if arr[i][j]:
#                 cnt += 1
#             else: # arr[i][j] == 0 이면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#     for i in range(N):
#         cnt = 0 # j열에서 연속한 1의 개수
#         for j in range(N):
#             if arr[i][j]:
#                 cnt += 1
#             else: # arr[i][j] == 0 이면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#     print(f'#{tc} {ans}')





# retry
import sys
sys.stdin = open('whereword.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    N += 1 # why. -> arr에 가로세로 0씩 추가했으니까 다음 포문의 탐색에서도 N+1값을 비교하기위해?

    result = 0 # 가로, 세로에서 구한거 더할 값
    for i in range(N):
        cnt = 0 # 세로 연속 3갯수
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else: #arr[i][j] == 0이면
                if cnt == K:
                    result += 1
                cnt = 0 # 초기화

    for j in range(N):
        cnt = 0 # 가로 연속 3갯수
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else: #arr[i][j] == 0이면
                if cnt == K:
                    result += 1
                cnt = 0 # 초기화

    print(f'#{tc} {result}')