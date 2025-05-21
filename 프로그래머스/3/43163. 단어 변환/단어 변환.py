from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def bfs(bigin, target, words):
        q = deque()
        q.append((begin, 0))
        
        visited = set()
        
        while q:
            cur, step = q.popleft()
            if cur == target:
                return step
            
            for word in words:
                if word not in visited and different(cur, word):
                    visited.add(word)
                    q.append((word, step+1))
        return 0
    
    def different(cur, word):
        cnt = 0
        for i in range(len(cur)):
            if cur[i] != word[i]:
                cnt += 1
        return cnt == 1
    
    return bfs(begin, target, words)