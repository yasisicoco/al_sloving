import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
result = 99999999999 # 최종비용

def back(cur, cnt, ans):
    global result

    if ans >= result:
        return
    
    if cnt == N:
        if lst[cur][0] != 0:
            result = min(result, ans+lst[cur][0]) # 출발도시로 돌아가는 값 더하기
        return
    
    for n in range(N):
        if not visited[n] and lst[cur][n] != 0:
            visited[n] = True
            back(n, cnt+1, ans+lst[cur][n])    
            visited[n] = False
        
visited[0] = True
back(0, 1, 0) # 0에서 출발 카운트 1

print(result)