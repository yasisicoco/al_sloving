import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 1001
lst[1] = 1
lst[2] = 3

for i in range(3, 1001):
    if i == 1 and i == 2:
        pass
    lst[i] = lst[i-1] + (lst[i-2] * 2)

print(lst[n]%10007)