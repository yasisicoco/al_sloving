import sys; sys.stdin = open('swea\\input\\1225.txt', 'r')

Q = [0] * 200000
front = rear = -1
def enQueue(item):
    global rear
    rear = rear + 1
    Q[rear] = item

def deQueue():
    global front
    front = front + 1
    return Q[front]

def empty():
    return front == rear

for _ in range(10):
    tc_num = int(input())
    arr = list(map(int, input().split()))

    # 큐초기화
    front = rear = -1
    for val in arr:
        enQueue(val)

    num = 1
    while Q[rear]: # 마지막 값이 0이 아닐동안
        # 맨 앞의 값을 가져온다.
        val = deQueue()
        val -= num
        if val < 0:
            val = 0
        enQueue(val)
        num = num + 1 if num < 5 else 1

    while not empty():
        print(f'{deQueue()}', end=' ')