import sys
t = int(sys.stdin.readline())
for i in range(t):
    k, r = map(int, sys.stdin.readline().split())
    print(k + r)