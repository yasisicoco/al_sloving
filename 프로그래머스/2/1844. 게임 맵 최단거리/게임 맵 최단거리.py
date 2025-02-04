def solution(maps):
    def bfs(si, sj):
        Queue = [(si, sj)]
        visited[si][sj] = 1
        
        while Queue:
            ci, cj = Queue.pop(0)
            if ci == col-1 and cj == row-1:
                return visited[col-1][row-1]
            
            for k in range(4):
                ki = ci + di[k]
                kj = cj + dj[k]
                if 0 <= ki < col and 0 <= kj < row:
                    if maps[ki][kj] == 1 and visited[ki][kj] == 0:
                        visited[ki][kj] = visited[ci][cj] + 1
                        Queue.append([ki, kj])
        return -1
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    col = len(maps)
    row = len(maps[0])
    visited = [[0] * row for _ in range(col)]
    result = bfs(0, 0)
    return result