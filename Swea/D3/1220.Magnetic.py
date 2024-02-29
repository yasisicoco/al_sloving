# 1220. Magnetic
# state 1
def check():
    global cnt
    cnt = 0
    for i in range(N):
        save = -1
        for j in range(N):
            # 만약 j행에서 1다음에 2가 나오면 +1 카운트
            if arr[j][i] == 1:
                save = 1
            elif arr[j][i] == 2:
                if save == 1:
                    save = -1
                    cnt += 1

T = 10
for tc in range(1, T+1):
    # 배열의 크기 N * N
    N = int(input())    
    # 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    check()
    print(f'#{tc} {cnt}')


# state 2
# 열검사 함수
# def get_sero_cnt(col):
#     cnt = 0
#     #red 자성체를 체크
#     is_red = False

#     for row in range(N):
#         #1. red 자성체 발견
#         if arr[row][col] == 1:
#             is_red = True
#         #2. 이전에 자성체를 발견했고, 현재 blue 자성체 발견 cnt += 1
#         elif is_red and arr[row][col] == 2:
#             cnt += 1
#             is_red = False # 갱신
#     return cnt

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     total_cnt = 0
#     # 열 순회하면서 total_cnt 누적
#     for col in range(N):
#         # cnt를 total_cnt 에 누적
#         total_cnt += get_sero_cnt(col)
#     print(f'#{tc} {total_cnt}')