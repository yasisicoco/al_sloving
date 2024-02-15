size = 5
Q = [0] * size
front=rear=0

def enQueue(item):
    global rear
    # 선형큐> full-check : rear == size -1
    # rear += 1
    # 원형큐> full =>
    if (rear+1) % size == front:
        print('Full!!!')
        return
    rear = (rear + 1) % size
    Q[rear] = item

def isEmpty():
    return front == rear

def deQueue():
    global front
    # empty-check 는 f == r
    # front += 1
    #
    front = (front + 1) % size
    return Q[front]

def empty():
    return front == rear

enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
print(Q)
print(front, rear)

while not empty():
    print(deQueue())