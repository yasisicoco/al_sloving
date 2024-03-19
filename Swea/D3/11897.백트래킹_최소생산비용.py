# state 1
def price(j):
    global result
    if len(lst) == N:
        if result >= sum(lst):
            result = sum(lst)
        return

    if result <= sum(lst):
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        lst.append(V[j][i])
        price(j+1)
        lst.pop()
        visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    result = 999999999999
    lst = []
    price(0)
    print(f'#{tc} {result}')


# state 2
def price(j, sumone):
    global result
    if j == N:
        if result >= sumone:
            result = sumone
        return
 
    if result <= sumone:
        return
 
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        k = V[j][i]
        price(j+1, sumone+k)
        visited[i] = False
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
 
    result = 999999999999
    price(0, 0)
    print(f'#{tc} {result}')