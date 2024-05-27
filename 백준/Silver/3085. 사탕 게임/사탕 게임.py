import sys
input = sys.stdin.readline

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

# 바꿀때마다 일렬로 최대길이 확인하기
def check():
    global result
    # 행 확인
    for i in range(N):
        cnt = 1  # 연속되는 사탕의 수
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1  # 연속이 끊기면 카운트를 1로 초기화

    # 열 확인
    for j in range(N):
        cnt = 1  # 연속되는 사탕의 수
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1  # 연속이 끊기면 카운트를 1로 초기화        

# 사탕 상하좌우로 바꾸기 (다를경우에만)
def change(si, sj):
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[si][sj] != arr[ni][nj]:
            arr[si][sj], arr[ni][nj] = arr[ni][nj], arr[si][sj]
            check()
            arr[si][sj], arr[ni][nj] = arr[ni][nj], arr[si][sj]

N = int(input().strip())
arr = []
for line in range(N):
    arr.append(list(input().strip()))

result = 0
for i in range(N):
    for j in range(N):
        change(i, j)

print(result)