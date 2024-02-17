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
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]: # 만약 맨앞 데이터가 제일 중요하다면
            cnt += 1 # 뽑기
            if queue[0][0] == M: # 뽑은게 내가 찾는거라면, queue[idx == M][i]
                print(cnt) # 프린트
                break
            else: # 아니라면
                queue.popleft() # 빼기
        else:
            queue.append(queue.popleft()) # 빼서 뒤로넣기