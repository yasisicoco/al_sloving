def dfs(frd, vis, cur, depth):
    if depth == 2:
        return
    
    for i in frd[cur]:
        if not vis[i]:
            vis[i] = True
        dfs(frd, vis, i, depth+1)

n = int(input())
m = int(input())
friends = [map(int, input().split()) for _ in range(m)]

frd = [[] for _ in range(n+1)]
vis = [False] * (n+1)
vis[1] = True

for a, b in friends:
    frd[a].append(b)
    frd[b].append(a)
    
dfs(frd, vis, 1, 0)
print(len([x for x in vis if x]) -1)