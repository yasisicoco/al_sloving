N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]

result = 0
for i in range(N):
    st = 0
    for j in range(M):
        if arr[i][j] == '0':
            st += 1
            if st >= K:
                result += 1
        elif arr[i][j] == '1':
            st = 0

print(result)