import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []

for _ in range(N):
    a, b = map(int, input().split())
    lst.append(b-a)

lst.sort()

if lst[K-1] < 0:
    print(0)
else:
    print(lst[K-1])