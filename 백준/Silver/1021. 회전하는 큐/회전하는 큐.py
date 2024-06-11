from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
num_lst = deque([i for i in range(1, N+1)]) # 1, ..., n

cnt = 0
for num in numbers:
    while True:
        if num_lst[0] == num:
            num_lst.popleft()
            break
        else:
            if num_lst.index(num) > len(num_lst) // 2:
                while num_lst[0] != num:
                    num_lst.appendleft(num_lst.pop())
                    cnt += 1
            else:
                while num_lst[0] != num:
                    num_lst.append(num_lst.popleft())
                    cnt += 1

print(cnt)