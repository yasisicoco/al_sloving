# state 2

# N까지의 자연수, 중복없이 M개
N, M = map(int, input().split())
# 부분집합용 리스트
arr = []
# 중복방지용 방문 (자연수가1부터니까 인덱스 +1)
visited = [False for _ in range(N+1)]

def recur(cur):
    global ans

    if len(arr) == M: # 부분집합길이가 M이 되면
        print(arr)
        return

    for i in range(cur, N+1): # 1부터 N까지의 자연수
        if visited[i]: # True
            continue
        visited[i] = True
        if i in arr:
            continue
        arr.append(i) # 부분집합 리스트로 추가
        recur(cur+1)
        arr.pop()
        visited[i] = False

recur(1)