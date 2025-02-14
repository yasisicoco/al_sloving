from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    result = [0] * m
    
    def getOil(si, sj):
        di = [0, 1, -1, 0]
        dj = [1, 0, 0, -1]
        q = deque()
        q.append((si, sj))
        visited[si][sj] = True
        size = 1
        affect_col = {sj}
        
        while q:
            ci, cj = q.popleft()
            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and land[ni][nj] == 1:
                    visited[ni][nj] = True
                    size += 1
                    q.append((ni, nj))
                    affect_col.add(nj)
                    
        for col in affect_col:
            result[col] += size
    
    # 열 이동하면서 시추작업 시작
    for j in range(m):
        for i in range(n):
            if not visited[i][j] and land[i][j] == 1:
                getOil(i, j)
        
    return max(result)