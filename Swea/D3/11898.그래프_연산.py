from collections import deque

def func(num, k):
    if k == 0:
        return num + 1
    if k == 1:
        return num - 1
    if k == 2:
        return num * 2
    if k == 3:
        return num - 10
    
def calc(num):
    q = deque()
    q.append(num)
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):            
            num2 = q.popleft()
            for k in range(4):
                result = func(num2, k)
                if result == M:
                    return cnt
                if 0 < result <= 1000000 and not visited[result]:
                    q.append(result)
                    visited[result] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print(f'#{tc}', calc(N))