<<<<<<< HEAD
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur):
    
    if visited[cur] == False:  # 만약에 방문한 곳이 아니면 링크에 0이 아닌 값 입력
        link[cur] = cur
    for j in v[cur]:
        if visited[j] == True:
            continue
        visited[j] = True
        cur = j # 지금장소는 i
        dfs(cur)
        
        
    
# 정점, 간선의 개수    
N, M = map(int, input().split())
# 인접정점    
v = [[] for _ in range(N+1)]
# 방문처리
visited = [False for _ in range(N+1)]

for _ in range(M): # 간선 수만큼
    a, b = map(int, input().split())
    v[a].append(b) # 무방향그래프
    v[b].append(a)

cnt = 0
link = [0] * (N+1) # 링크 리스트를 만들어서 들린곳을 표시, 같은 연결정점은 같은수로 표시
for i in range(1, N+1):
    dfs(i)
for i in range(1, N+1):
    if link[i] != 0: # 순회중 만약 link가 0이 아닌게 있다면 cnt+=1
        cnt += 1
print(cnt)
=======
>>>>>>> 3749e6a7d99a5cb321d9f6b13849cf04cf72bc9e
