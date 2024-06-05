import sys
input = sys.stdin.readline

def fly(start, cnt):
    visited[start] = True
    
    for next in arr[start]:
        if visited[next] == False:
            cnt = fly(next, cnt+1)
    return cnt

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    visited = [False for _ in range(N+1)]
    arr = [[] for _ in range(N+1)]
    
    visited[0] = True
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    result = 10e9
    result = fly(1, 0)
    print(result)