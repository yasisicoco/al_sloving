from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # print(rectangle, characterX, characterY, itemX, itemY)
    
    def make_road(rectangles, road):
        for rec in rectangles:
            # x1, y1, x2, y2 = rec[0], rec[1], rec[2], rec[3]
            x1, y1, x2, y2 = [x * 2 for x in rec]
            for i in range(y1, y2+1):
                road[i][x1] = True #좌변
                road[i][x2] = True #우변
            for j in range(x1, x2+1):
                road[y1][j] = True #아랫변
                road[y2][j] = True #윗변               
        
        for rec in rectangles:
            x1, y1, x2, y2 = [x * 2 for x in rec]
            for i in range(y1+1, y2):
                for j in range(x1+1, x2):
                    road[i][j] = False
        return road
    
    def bfs(si, sj, ei, ej):
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상
        visited = [[False] * 102 for _ in range(102)]
        q = deque()
        q.append((si, sj, 0))
        visited[si][sj] = True
        
        while q:
            ci, cj, cnt = q.popleft()
            if ci == ei and cj == ej:
                return cnt//2
            
            for k in range(4):
                ni, nj = ci+di[k], cj+dj[k]
                if 0 <= ni < 102 and 0 <= nj < 102 and not visited[ni][nj] and road[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj, cnt+1))
                
    road = [[False] * 102 for _ in range(102)]
    make_road(rectangle, road)
    result = bfs(characterY*2, characterX*2, itemY*2, itemX*2)
    # print(result)
    
    return result