def recur(level, sumone):
    global result

    if level == N:
        if result < sumone:
            result = sumone
        return

    if result >= sumone:
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        recur(level+1, sumone*(arr[level][i]/100))
        visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    result = 0
    recur(0, 1)
    print(f'#{tc} {(result*100):0.6f}')
