import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

nx = (p + t) % (2 * w)
ny = (q + t) % (2 * h)

if nx <= w:
    x = nx
else:
    x = 2 * w - nx

if ny <= h:
    y = ny
else:
    y = 2 * h - ny

print(x, y)
