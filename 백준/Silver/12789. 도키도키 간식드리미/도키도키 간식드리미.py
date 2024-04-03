from collections import deque

N = int(input())
line = list(map(int, input().split()))

line = deque(line)
lst = []

cnt = 1
result = True
while line or lst: # 줄이 남아있는 동안
    if not line and lst[-1] != cnt: # 기존 줄이 없고 임시줄은 있는데 순서가 아닌경우
        result = False
        break

    if line and line[0] == cnt:
        line.popleft()
        cnt += 1
        continue
    elif lst and lst[-1] == cnt:
        lst.pop()
        cnt += 1
        continue
    
    if line[0] != cnt or (lst and lst[-1] != cnt):
        k = line.popleft()
        lst.append(k)

if result == False:
    print("Sad")
else:
    print("Nice")