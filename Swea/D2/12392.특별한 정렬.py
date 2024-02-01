import sys
sys.stdin = open('special_arr.txt')

# 1차시
# T = int(input()) 
# for tc in range(1, T+1): # 테스트 케이스 반복
#     N = int(input()) # 정수의 개수
#     ai = list(map(int, input().split())) # N개의 정수를가진 리스트

#     for i in range(N-1):
#         if i % 2 == 0:
#             max_idx = i
#             for j in range(i+1, N):
#                 if ai[max_idx] < ai[j]:
#                     max_idx = j
#                 ai[i], ai[max_idx] = ai[max_idx], ai[i]
#         if i % 2 == 1:
#             min_idx = i
#             for j in range(i+1, N):
#                 if ai[min_idx] > ai[j]:
#                     min_idx = j
#                 ai[i], ai[min_idx] = ai[min_idx], ai[i]
    
#     print(f'#{tc} {ai}')



# 2차시
# T = int(input()) 
# for tc in range(1, T+1): # 테스트 케이스 반복
#     for i in range(N-1):
#         max_idx = i
#         min_inx = i
#         for j in range(i+1, N):
#             if max_idx % 2 == 0:
#                 if ai[max_idx] < ai[j]:
#                     max_idx =j
#                 ai[i], ai[max_idx] = ai[max_idx], ai[i]
#             if min_idx % 2 == 1:
#                 if ai[min_idx] < ai[j]:
#                     min_idx =j
#                 ai[i], ai[min_idx] = ai[min_idx], ai[i]
                
#     print(f'#{tc} {ai}')



# 3차시
T = int(input()) 
for tc in range(1, T+1): 
    N = int(input()) 
    ai = list(map(int, input().split())) 

    for i in range(N-1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i+1, N): # 현재 인덱스부터 끝까지 돌면서 가장 큰 값을 찾음
                if ai[max_idx] < ai[j]:
                    max_idx = j
            ai[i], ai[max_idx] = ai[max_idx], ai[i] # 가장 큰 값을 현재 위치로 이동
        else:  # if i % 2 == 1
            min_idx = i
            for j in range(i+1, N): # 현재 인덱스부터 끝까지 돌면서 가장 작은 값을 찾음
                if ai[min_idx] > ai[j]:
                    min_idx = j
            ai[i], ai[min_idx] = ai[min_idx], ai[i] # 가장 작은 값을 현재 위치로 이동
    ai = ai[:10]
        
    print(f'#{tc}', *ai)