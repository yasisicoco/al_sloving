T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * N for _ in range(N)]

    di = 0
    dj = 0
    k = 0
    for r in range(N):
        for c in range(N):   
            di = r + dr[k]
            dj = c + dc[k]
            arr[di][dj] += 1
            


# 다율누나 코드
# T = int(input())
# for tc in range(1, T + 1):
#     dr = [0, 1, 0, -1]  # 우하좌상
#     dc = [1, 0, -1, 0]
#     N = int(input())
#     fix_N = N
#     arr = [[0] * N for _ in range(N)]

#     num = 1 빈 배열을 채울 조건 
#     r = 0
#     c = 0

#     dir = 3
#     while N > 1:
#         if N == fix_N:
#             arr[0][0] = num
#             for i in range(3):
#                 dir = (dir + 1) % 4  # Change direction
#                 for j in range(N - 1):
#                     r += dr[dir]
#                     c += dc[dir]
#                     if 0 <= r < N and 0 <= c < N:
#                         num += 1
#                         arr[r][c] = num

#             N -= 1
#         else:
#             for k in range(2):
#                 dir = (dir + 1) % 4  # Change direction
#                 if k == 0:
#                     k = 1
#                 for l in range(N - k):
#                     r += dr[dir]
#                     c += dc[dir]
#                     if 0 <= r < fix_N and 0 <= c < fix_N:
#                         num += 1
#                         arr[r][c] = num
#             N -= 1

#     print(f"#{tc}")
#     for line in arr:
#         print(*line)