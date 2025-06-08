from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deck = deque()
for _ in range(n):
    order = input().split()

    if order[0] == 'push_front':
        deck.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        deck.append(int(order[1]))
    elif order[0] == 'pop_front':
        if not deck:
            print(-1)
            continue
        w = deck.popleft()
        print(w)
    elif order[0] == 'pop_back':
        if not deck:
            print(-1)
            continue
        w = deck.pop()
        print(w)
    elif order[0] == 'size':
        print(len(deck))
    elif order[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not deck:
            print(-1)
            continue
        print(deck[0])
    elif order[0] == 'back':
        if not deck:
            print(-1)
            continue
        print(deck[-1])