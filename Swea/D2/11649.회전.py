# state 1. deque()
# import sys
# sys.stdin = open('al_sloving\\swea\\input\\11649.txt', 'r')
# from collections import deque

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N개로 이루어진 수열, 뒤로M번 보내기
#     cQ = list(map(int, input().split())) # 자연수 N개
#     cQ = deque(cQ)

#     for i in range(M):
#         result = cQ.popleft()
#         cQ.append(result)
    
#     print(f'#{tc} {cQ.popleft()}')


# 정종윤 강사님 state
import sys
sys.stdin = open('al_sloving\\swea\\input\\11649.txt', 'r')

def enQueue(item):
    global rear
    rear = (rear + 1) % (N+1) # tc1, N==4
    Q[rear] = item

def deQueue():
    global front
    front = (front + 1) % (N+1)
    return Q[front]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N개로 이루어진 수열, 뒤로M번 보내기
    Q = [0] * (N+1) # 큐!!! [0, x, x, x, ...]
    front = rear = 0 # 원형!
    cQ = list(map(int, input().split())) # 자연수 N개

    for i in cQ:
        enQueue(i)

    for _ in range(M):
        tmp = deQueue()
        enQueue(tmp)

    print(f'#{tc} {Q[(front+1) % len(Q)]}')