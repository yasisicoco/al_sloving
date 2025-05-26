import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

if n == 1:
    for row in arr:
        print(''.join(row))
    exit()

def full_bomb():
    return [['O'] * c for _ in range(r)]

def boom(arr):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    boom = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                boom[i][j] = True
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < r and 0 <= nj < c:
                        boom[ni][nj] = True

    for i in range(r):
        for j in range(c):
            if boom[i][j]:
                arr[i][j] = '.'
            else:
                arr[i][j] = 'O'
    return arr

if n % 2 == 0:
    result = full_bomb()
elif n % 4 == 3:
    copy = [row[:] for row in arr]
    result = boom(copy)
elif n % 4 == 1:
    copy = [row[:] for row in arr]
    first_boom = boom(copy)
    copy2 = [row[:] for row in first_boom]
    result = boom(copy2)

for row in result:
    print(''.join(row))