import sys
input = sys.stdin.readline

# 현재 500
# 하루에 K씩 줄음
# N일 동안 500이하가 되지않도록

N, K = map(int, input().split())
kit = list(map(int, input().split()))
def check(kg, n):
    global result
    if kg < 500:
        return
    if n == N:
        result += 1
        return
    kg -= K
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            check(kg+kit[i], n+1)
            visited[i] = False
today=500
result = 0
visited = [False] * N
check(500, 0)
print(result)