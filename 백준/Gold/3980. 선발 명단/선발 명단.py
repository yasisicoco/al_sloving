import sys
input = sys.stdin.readline

def back(idx, stat):
    global result
    
    if idx == 11:
        result = max(stat, result)
        return
        
    for i in range(11):
        if visited[i] or players[idx][i] == 0:
            continue
        
        visited[i] = True
        back(idx+1, stat + players[idx][i])
        visited[i] = False

#---------------------------------------------------------------------

T = int(input())
for tc in range(T):
    
    players = [list(map(int, input().split())) for _ in range(11)]
    visited = [False for _ in range(11)]
    result = -10e9
    
    back(0, 0)
    print(result)