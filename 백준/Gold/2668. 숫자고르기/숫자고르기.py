def dfs(cur, k):
    visited[cur] = True
    
    for i in lst[cur]:
        if not visited[i]:
            dfs(i, k)
            
        elif visited[i] and k == i:
            ans.append(i)
        

N = int(input())
lst = []
for _ in range(N):
    lst.append([int(input())])
lst = [0] + lst

ans = []
for k in range(1, N+1):
    if k == lst[k]:
        ans.append(k)

for k in range(1, N+1):
    visited = [False] * (N+1)
    dfs(k, k)

ans.sort()
print(len(ans))
for j in range(len(ans)):
    print(ans[j])