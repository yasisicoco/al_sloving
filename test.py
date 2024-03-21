# 백준. 숫자고르기

N = int(input())
fir = [0] + [i for i in range(1, N+1)]
v = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    v[i] = num

print(fir); print(v); print(visited)

def dfs(cur):

    for i in fir[cur]:
        if visited[i]:
            continue
        visited[i] = True
        cur = i
        
        dfs(cur)