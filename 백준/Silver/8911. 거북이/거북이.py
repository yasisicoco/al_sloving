import sys
input = sys.stdin.readline

di = [0, 1, 0, -1] # 0: 동 1: 남 2: 서 3: 북
dj = [1, 0, -1, 0]
dir = 0
T = int(input())

for i in range(T):
    commend = input().strip()
    start = [0, 0]
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    
    for c in commend:
        if c == 'F':
            start[0] += di[dir]
            start[1] += dj[dir]
        elif c == 'B':
            start[0] -= di[dir]
            start[1] -= dj[dir]
        elif c == 'L':
            dir = (dir - 1) % 4
        elif c == 'R':
            dir = (dir + 1) % 4
            
        min_x = min(min_x, start[0])
        max_x = max(max_x, start[0])
        min_y = min(min_y, start[1])
        max_y = max(max_y, start[1])
        
    print(abs(max_x - min_x) * abs(max_y - min_y))
        