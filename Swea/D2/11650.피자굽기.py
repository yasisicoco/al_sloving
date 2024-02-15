import sys
sys.stdin = open('/swea/input/11650.txt', 'r')

# N개의 피자를 동시에 구움
# 1번부터 M번까지 피자를 순서대로 화덕에 넣음
# 치즈가 녹는시간이 다르다.
# 꺼내는 순서는 바뀔 수 있음
# 조건
# 화덕에 가장 마지막까지 남아있는 피자번호 구하기

from collections import deque

# 피자굽기
T = int(input())
for tc in range(1, T+1):
    size, pizza = map(int, input().split())
    cheeze = map(int, input().split())
    Q = [] * size
    Q = deque(Q)

    for i in cheeze:
        Q.append(i)
        if len(Q) == 3:
            check = Q.popleft()

            while len(check) == 3:
                if check != 0:
                    check = check // 2
                    Q.append(check)
                else:
                    pass