# state1
import sys
sys.stdin = open('1219.txt', 'r')

for tc in range(1, 11):
    T, E = map(int, input().split())
    
    v = [[] for _ in range(101)]
    visited = [False for _ in range(101)]
    
    lst = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        a, b = lst[i], lst[i+1]
        v[a].append(b) # 유향 그래프
    
    result = 0
    def dfs(cur, end):
        global result
        for k in v[cur]:
            if visited[k]:
                continue
            visited[k] == True
            if k == end:
                result = 1
            cur = k
            dfs(cur, end)
        else:
            return result

    # dfs(cur, R) 현재 == 0, 도착점 == 99
    result = dfs(1, 99)
    
    print(f'#{tc} {result}')