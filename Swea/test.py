#지그재그
# N = 5
# arr = [[0] * N for _ in range(N)]
#
# num = 1
# for r in range(N):
#     if r % 2 == 0:
#         for c in range(N):
#             arr[r][c] = num
#             num += 1
#     else:
#         for c in range(N-1, -1, -1):
#             arr[r][c] = num
#             num += 1
#
# for line in arr:
#     print(*line)

# 대각
# N = 5
# arr = [[0] * N for _ in range(N)]
#
# for r in range(N):
#     arr[r][r] = 1
#
# for r in range(N):
#     arr[r][N-1 - r] = 2
#
# for line in arr:
#     print(*line)


# 대각경계선 양쪽
# N = 5
# arr = [[0] * N for _ in range(N)]
#
# for r in range(N):
#     for c in range(r + 1, N):
#         arr[r][c] = 1
#
# for r in range(N):
#     for c in range(c + 1, N):
#         arr[r][c] = 1
#
# for line in arr:
#     print(*line)


# 가운데만
# N = 5
# arr = [[0] * N for _ in range(N)]
#
# for r in range(1, N - 1):
#     for c in range(1, N - 1):
#         arr[r][c] = 1
#
# for line in arr:
#     print(*line)


# delta_array 연습문제 1-2
# 배열 만들기
N = 5
arr = [[0] * N for _ in range(N)]
num = 1

for r in range(0, N):
    for c in range(0, N):
        arr[r][c] = num
        num += 1
for line in arr:
    print(*line)

# 델타인덱스 이용하여 주변수 더하기 (요소 총 25개)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
result = 0
for r in range(N):
    for c in range(N):
        total_sum = arr[r][c]
        for k in range(4):  # 0, 1, 2, 3 #조작키 범위 3부터 시계방향
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N: #인덱스벨류 오류 피하기
                total_sum += arr[nr][nc]
                result += total_sum

print(result)