import sys
from collections import deque
input = sys.stdin.readline

# F층건물,S지금층,G목적지,U업,D다운
# 버튼을 몇번 눌러야하는지 출력, 못가는 곳은 use the stairs

F, S, G, U, D = map(int, input().split())

visited = [False] * (F+1)

q = deque()
q.append((S, 0))
visited[S] = True

while q:
    cur, cnt = q.popleft()

    if cur == G:
        print(cnt)
        break

    # up
    next_up = cur + U
    if next_up <= F and not visited[next_up]:
        visited[next_up] = True
        q.append((next_up, cnt+1))
    # down
    next_down = cur - D
    if next_down >= 1 and not visited[next_down]:
        visited[next_down] = True
        q.append((next_down, cnt+1))
    
else:
    print("use the stairs")