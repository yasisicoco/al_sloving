# 1차 시도
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
    
#     result = 0
#     for i in range(N):
#         r = 0 + i
#         c = 0 + i
#         sum = 0
#         for r in range(M):
#             for c in range(M):    
#                 sum += arr[r][c]
#         if sum >= result:
#             result = sum
#     print(f'#{tc} {result}')
    
    
# 2차 시도
# import sys
# sys.stdin = open('paris.txt')

# '''
# 10
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
# '''

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
    
    
#     dr = [0, 1, 1]
#     dc = [1, 0, 1]
#     result = 0
#     for r in range(N):
#         for c in range(N):
#             number = 0
#             for r in range(M):
#                 for c in range(M):
#                     if 0 <= r < N and 0 <= c < N:    
#                         number += arr[r][c]
#                     for k in range(3):
#                         r = r + dr[k]
#                         c = c + dc[k]
#                         if 0 <= r < N and 0 <= c < N:    
#                             number += arr[r][c]
#             if number >= result:
#                 result = number
#     print(f'#{tc} {result}')




# 3차 시도

import sys
sys.stdin = open('paris.txt')

'''
10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        
    result = 0
    for i in range(N - M + 1): # 5 - 2 / 0 1 2
        for j in range(N - M + 1): # 5 - 2 / 0 1 2
            kill = 0
            
            for r in range(i, i + M): # 2 + 2 / 0 1 2 3
                for c in range(j, j + M):
                    kill += arr[r][c]
            if result < kill:
                result = kill
    print(f'#{tc} {result}')
    