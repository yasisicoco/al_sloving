from collections import deque
from sys import stdin
input = stdin.readline
 
dq = deque()

def dus(cur): # cur는 튜플자료형일 수 있다.
    if cur[0] == 'pop':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif cur[0] == 'size':
        print(len(dq))
    elif cur[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif cur[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif cur[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])
    else:
        dq.append(cur[1])


N = int(input())
for _ in range(N):
    a = list(input().split())

    # 현 스택의 가장 왼쪽을 출력
    dus(a)