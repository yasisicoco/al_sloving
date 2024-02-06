# state 1
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())


#     arr = []
#     for _ in range(N):
#         str_r = input()
#         # str_r_lst = list(str_r)
#         arr.append(str_r)
#     print(arr)
    
#     # N-M+1 까지 돌면서 확인할것
#     # M-i+1 // 2 까지만 회문 확인

#     for i in range(N):
#         for j in range(i, (M-i+1)//2):
#             if arr[i][j] == arr[i][M-1-j]:
#                 result = 1
#             else:
#                 result = 0
#                 break
#         if result == 1:
#             print(arr[i][j::])


# state 2
import sys
sys.stdin = open('D2문자열회문.txt')
T = int(input())
for tc in range(1, T+1):
    # N : N*N크기의 글자판, M : 회문의 길이
    N, M = map(int, input().split())
    # arr = 글자판
    arr = [list(input()) for _ in range(N)]

    result = None
    for i in range(N):
        for k in range(N-M+1):
            di = arr[i][k:k+M] # 가로 확인 변수
            dj = [] # 세로 확인 변수
            for j in range(k, k+M): # 문자열 인덱스 0부터 M까지
                dj.append(arr[j][i])
            if di == di[::-1]:
                result = di
            if dj == dj[::-1]:
                result = dj
    
    print(*result, sep='')