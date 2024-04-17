import sys
N = int(input())
bd = []
for _ in range(N):
    bd.append(int(sys.stdin.readline()))
bd.reverse()
stack = []
stack.append(bd.pop())

sumone = 0
while bd:
    if not stack:
        stack.append(bd.pop())
    elif bd[-1] < stack[-1]:
        sumone += len(stack)
        stack.append(bd.pop())
    else:
        stack.pop()

print(sumone)