import sys
input = sys.stdin.readline

def dfs(cur):
    global st
    if cur == v[cur][0]:
        st.add(cur)
    
    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        if cur == v[i][0]:
            st.add(v[i][0])
        dfs(i)
        
N = int(input())
v = [[0]]


for _ in range(N):
    a = int(input())
    v.append([a])

st = set()
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    dfs(i)

print(len(st))
for j in st:
    print(j)