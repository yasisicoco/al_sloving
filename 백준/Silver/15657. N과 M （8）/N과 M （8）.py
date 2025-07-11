import sys
input = sys.stdin.readline

def back(start, cur):
    if len(cur) == M:
        print(*cur)
        return
    for i in range(start, N):
        cur.append(lst[i])
        back(i, cur)
        cur.pop()

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
back(0, [])