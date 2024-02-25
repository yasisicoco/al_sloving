# dfs start
def dfs(s, g):
    # 스택
    st = []
    visited[s] = True # 시작점 방문
 
    while True:
        for i in v[s]:
            if visited[i] == False:
                st.append(s) # 스택에 출발지추가
                s = i # 이동
                if s == g: # 이동지가 g(도착지)라면?
                    return 1 
                else:
                    visited[i] = True # 아니면 도착도장만
                    break
        else: # 도착도장있는곳이면
            if st: 
                s = st.pop()
            else:
                return 0
 
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V개의 노드, E개의 간선
 
    # 그래프 탐색에서 제일먼저 인접리스트를 만들자
    v = [[] for _ in range(V+1)]
    # 방문처리 (visited 배열)
    visited = [False for _ in range(V+1)]
 
    for _ in range(E): # edge개의 출발, 도착 간선노드가 주어짐
        a, b = map(int, input().split())
        v[a].append(b)
    # 출발노드, 도착노드 입력
    S, G = map(int, input().split())
 
 
    result = dfs(S, G)
    print(f'#{tc} {result}')
    
    
    
# state 2
def dfs(cur, g):
    global result
    visited[cur] = True
    
    for i in v[cur]:
        if visited[i] == True:
            continue
        visited[i] = True
        cur = i
        if cur == g:
            result = 1
        dfs(cur, g)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    # 인접정점리스트
    v = [[] for _ in range(V+1)]
    # 방문확인
    visited = [False for _ in range(V+1)]
    
    for i in range(E):  # 간선정보
        a, b = map(int, input().split())
        v[a].append(b) # 방향존재
    
    result = 0
    S, G = map(int, input().split()) # 출발 노드S, 도착 노드G
    dfs(S, G)
    print(f'#{tc} {result}')