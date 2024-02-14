import sys
sys.stdin = open('11614.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 인원수N
    card = list(map(int, input().split())) # N명이 고른 카드


def win(s, e):  # 매개변수를 시작과 끝으로 호출
    if s == e:  # 기저함수, 시작과 끝이 같아지면 호출(s)
        return s
    
    else:
        mid = (s + e) // 2
        if len(mid) == 2:
            for i in mid:
                card[i]


        # a = win(s, mid)
        # b = win(mid + 1, e)


win(0, N-1)



























# 강사님 힌트
# arr = [5, 7, 8, 2, 4, 6, 9, 3]
# N = len(arr)
# # 최대값 구하기
# def find_max(s, e):
#     if s == e:
#         return s
#         # return arr[s]
#     else:
#         mid = (s + e) // 2
#         a = find_max(s, mid)
#         b = find_max(mid + 1, e)
#         return a if arr[a] > arr[b] else b

# idx = find_max(0, N - 1)
# print(idx, arr[idx])