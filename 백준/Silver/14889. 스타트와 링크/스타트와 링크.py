import sys
input = sys.stdin.readline

def back(depth, idx):
    global result
    if depth == N // 2:
        L = 0
        S = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    L += arr[i][j]
                elif not visited[i] and not visited[j]:
                    S += arr[i][j]
        result = min(abs(L-S), result)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            back(depth+1, i+1)
            visited[i] = False
        
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
result = 10e9

back(0, 0)
print(result)