r, c= map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(input()))

# print(arr)
di, dj = [0, 1, -1, 0], [1, 0, 0, -1]
def escape(fire):
    q = []
    q.append((ji, jj, 0))
    fire_q = []
    fire_q.extend(fire)
    visited = [[False] * c for _ in range(r)]
    visited[ji][jj] = True

    while q:
        fire_size = len(fire_q)
        for _ in range(fire_size):
            ci, cj = fire_q.pop(0)
            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]
                if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != 'F' and arr[ni][nj] != '#':
                    arr[ni][nj] = 'F'
                    fire_q.append((ni, nj))
        
        q_size = len(q)
        for _ in range(q_size):
            ci, cj, cnt = q.pop(0)

            if ci == 0 or ci == r-1 or cj == 0 or cj == c-1:
                return cnt + 1

            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]
                if 0 <= ni < r and 0 <= nj < c and not visited[ni][nj] and arr[ni][nj] == '.':
                    visited[ni][nj] = True
                    q.append((ni, nj, cnt+1)) 

    return 'IMPOSSIBLE'
            
ji = 0
jj = 0
fire = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            ji = i
            jj = j
        elif arr[i][j] == 'F':
            fire.append((i, j))

print(escape(fire))
