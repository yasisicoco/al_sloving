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
# N = 5
# arr = [[0] * N for _ in range(N)]
# num = 1

# for r in range(0, N):
    # for c in range(0, N):
        # arr[r][c] = num
        # num += 1
# for line in arr:
    # print(*line)

# 델타인덱스 이용하여 주변수 더하기 (요소 총 25개)
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# result = 0
# for r in range(N):
    # for c in range(N):
        # total_sum = arr[r][c]
        # for k in range(4):  # 0, 1, 2, 3 #조작키 범위 3부터 시계방향
            # nr = r + dr[k]
            # nc = c + dc[k]
            # if 0 <= nr < N and 0 <= nc < N: #인덱스벨류 오류 피하기
                # total_sum += arr[nr][nc]
                # result += total_sum

# print(result)


# 14425
# N, M = map(int, input().split())
# S = []
# for _ in range(N): # N 번의 반복
    # str1 = input() # 동안 문자열 한개씩
    # S.append(str1) # 집합 S에 추가

# cnt = 0 # 집합 S에 포함된 문자열의 갯수
# for _ in range(M):
    # str2 = input()
    # if str2 in S:
        # cnt += 1
# print(cnt)

# 2738
# N, M = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# B = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
    # for j in range(M):
        # A[i][j] += B[i][j]

# for line in A:
    # print(*line)


# 2851

# lst = []
# for tc in range(10):
#     N = int(input())
#     lst.append(N)

# max_val = 0
# num = len(lst)
# for i in range(0, num):
#     max_val += lst[i]
#     if max_val > 100:
#         real_i = i
#         break
# realmax = max_val - 100
# fakemax = 100 - (max_val - lst[real_i])
# if abs(100 - realmax) <= abs(100 - fakemax):
#     print(max_val)
# else:
#     print(max_val - lst[real_i])


#10789
strlst = []

for _ in range(5): # 5번 반복
    text = input()
    strlst.append(text) # 리스트에 str문자열추가

lst = []
for i in range(15): # 5번 돌면서
    for j in range(15):
        try:
            lst.append(strlst[j][i])
        except:
            continue
    else:
        continue

print(''.join(lst))