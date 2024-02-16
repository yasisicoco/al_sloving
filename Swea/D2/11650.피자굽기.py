# import sys
# sys.stdin = open('/swea/input/11650.txt', 'r')

# N개의 피자를 동시에 구움
# 1번부터 M번까지 피자를 순서대로 화덕에 넣음
# 치즈가 녹는시간이 다르다.
# 꺼내는 순서는 바뀔 수 있음
# 조건
# 화덕에 가장 마지막까지 남아있는 피자번호 구하기

# from collections import deque

# # 피자굽기
# T = int(input())
# for tc in range(1, T+1):
#     size, pizza = map(int, input().split())
#     cheeze = map(int, input().split())
#     Q = [] * size
#     Q = deque(Q)

#     for i in cheeze:
#         Q.append(i)
#         if len(Q) == 3:
#             check = Q.popleft()

#             while len(check) == 3:
#                 if check != 0:
#                     check = check // 2
#                     Q.append(check)
#                 else:
#                     pass

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    pizza = deque() 
    oven = deque()

    #n개의 피자를 오븐에 삽입
    for i in range(N):
        oven.append((i+1, arr[i]))
    
    #남은 피자정보를 pizza에 추가
    for j in range(N, M):
        pizza.append((j+1, arr[j]))

    while oven:
        num, cheeze = oven.popleft()
        cheeze //=2
        if cheeze > 0:
            oven.append((num, cheeze))
        else:
            if pizza:
                oven.append(pizza.popleft())

    print(f'#{tc} {num}')