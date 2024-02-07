# state 1
# def stackZero(n):
#     if 0 not in n: #함수멈추기
#         return arr_result
#     else:
#         for i in range(1, len(n)+1):
#             if n[i] != 0:
#                 pass
#             else: # 0이 나오면
#                 n[i-1].pop()
#         return arr_result
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = stackZero(arr)
#     print(f'#{tc} {result}')


# state 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in list(map(int, input().split())):
        if i != 0:
            arr.append(i)
        else:
            arr.pop()

    result = 0
    for j in arr:
        result += j

    print(f'#{tc} {result}')
