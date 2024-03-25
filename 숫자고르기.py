# 백준. 숫자고르기

def dfs(cur):

    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i)

N = int(input())
v = [[] for _ in range(N+1)]
visited = [0] * (N+1)

# 숫자 받기
for i in range(1, N+1):
    num = int(input())
    v[i] = num

# print(fir); print(v)
for i in range(1, N+1):
    