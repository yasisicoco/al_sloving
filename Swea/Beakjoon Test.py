<<<<<<< HEAD
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 문서의 개수, 궁금문서 idx
    lst = list(map(int, input().split()))
    queue = deque()

    for idx, i in enumerate(lst):
        queue.append((idx, i))
    
    cnt = 0
    while True:
        impo = -1
        for j in queue: # 최고중요도 탐색
            if j[1] > impo:
                impo = j[1]
        if queue[0][1] == impo: # 만약 맨앞 데이터가 제일 중요하다면
            cnt += 1 # 뽑기
            if queue[0][0] == M: # 뽑은게 내가 찾는거라면, queue[idx == M][i]
                print(cnt) # 프린트
                break
            else: # 아니라면
                queue.popleft() # 빼기
        else:
            queue.append(queue.popleft()) # 빼서 뒤로넣기
=======
def bfs(si, sj):
    global N, M
    Queue = []
    Queue.append((si, sj))
    visited[0][0] = 1
    
    while Queue:
        ci, cj = Queue.pop(0)
        for k in range(4):
            ki = ci + di[k]
            kj = cj + dj[k]
            if 0 <= ki < N and 0 <= kj < M:
                if arr[ki][kj] == 1 and visited[ki][kj] == 0:
                    visited[ki][kj] = visited[ci][cj] + 1
                    Queue.append((ki, kj))
                    if ki == (N-1) and kj == (M-1):
                        print(visited[ki][kj])
                        break


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
start_i, start_j = (0, 0) # 시작점 설정
bfs(start_i, start_j)
>>>>>>> 482728a5a2b20c6a489ca631d044553b43319f77
