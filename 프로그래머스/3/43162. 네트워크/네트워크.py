def solution(n, computers):
    # 방문리스트를 만들어서 이미 방문한곳이면 그냥 지나쳐가기,
    # 새롭게 방문하는곳이면 count+1 하여 네트워크 갯수를 센다.
    
    # 방문리스트
    global visited
    visited = [False for _ in range(n)]
    # count
    cnt = 0
    
    def dfs(cur):
        visited[cur] = True
        for i in range(n):
            if computers[cur][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if visited[i] == True:
            continue
        dfs(i)
        cnt += 1
        
    return cnt