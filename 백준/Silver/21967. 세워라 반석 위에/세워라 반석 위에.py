from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

maxdq = deque()
mindq = deque()

left = 0
ans = 0

for right in range(N):
    while maxdq and arr[maxdq[-1]] < arr[right]:
        maxdq.pop()
    maxdq.append(right)

    while mindq and arr[mindq[-1]] > arr[right]:
        mindq.pop()
    mindq.append(right)

    while arr[maxdq[0]] - arr[mindq[0]] > 2:
        if maxdq[0] == left:
            maxdq.popleft()
        if mindq[0] == left:
            mindq.popleft()
        left+=1
    ans = max(ans, right-left+1)

print(ans)