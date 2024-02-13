# T = int(input())
# for tc in range(1, T+1):
    # V, E = map(int, input().split())
    # arr = list(map(int, input().split()))
    # 
    # G = [[] for _ in range(V + 1)]
    # for i in range(0, E*2, 2):
        # u, v = G[i], G[i+1]
        # G[u].append(V) # 유향그래프
# 
    # S, G = map(int, input().split())
    # for j in range(1, V+1):
        # print(j, '-->', G[j])
    


'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# def dfs(i, V): # 시작 i, 마지막 V
    # visited = [0] * (V+1) #visited, stack 생성 및 초기화
    # st = []
    # visited[i] = 1  # 시작점 방문
    # print(i)        # 정점에서 할 일
    # while True: # 탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점w 있으면
        # for w in adjl[i]:
            # if visited[w] == 0:
                # st.append(i)    # push(i), i를 지나서
                # i = w           # w에 방문
                # visited[i] = 1  # 방문해서 할일
                # print(i)
                # break   # for w
        # # else:                   # for w, i에 남은 인접 정점이 없으면
            # # if st:    # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
                # i = st.pop()
            # # else:   # 스택이 비어있으면 (출발점에서 남은 정점이 없으면)
                # break   # while True
    # return
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# 
# 인접리스트
# # adjl = [[] for _ in range(V+1)] # ardjl[i] 행에 i에 인접인 정점번호
# for i in range(E):
    # n1, n2 = arr[i*2], arr[i*2+1]
    # adjl[n1].append(n2)
    # adjl[n2].append(n1) #방향이 없는 경우
# visited = [0]*(V+1) #visited, stack 생성 및 초기화
# dfs(1, V)
# 



# 1222
# import sys
# sys.stdin = open('', 'r')
# T = 10
# for tc in range(1, T+1):
        # print(f'#{tc}', end=' ')
        # 테스트 케이스 출력부분을 두고,
        # 그 끝을 개행문자 (end='\n')대신
        # 스페이스 출력
        # 풀이 1
        # _ = input() # 안쓸거지만 전체 길이가 주어짐
        # arr = input().split('+')
        # print(arr)
        # 

# 미로
# T = int(input())
#  
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#  
# def maze(start_y, start_x):
#  
    # global result
#  
    # for k in range(4):
        # new_y = start_y + dr[k]
        # new_x = start_x + dc[k]
#  
        # if 0 > new_x or new_x >= N or 0 > new_y or new_y >= N:
            # continue
        # elif int(arr[new_y][new_x]) == 0 and visited[new_y][new_x] == 0:
            # visited[new_y][new_x] = 1
            # maze(new_y, new_x)
        # elif int(arr[new_y][new_x]) == 3:
            # result = 1
            # return result
    # return result
#  
# for tc in range(1, T + 1):
#  
    # N = int(input())
    # arr = [list(input()) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    # result = 0
    # for i in range(N):
        # for j in range(N):
            # if int(arr[i][j]) == 2:
                # start_y = i
                # start_x = j
                # break
    # print(f'#{tc} {maze(start_y, start_x)}')




# 미로
# import sys
# sys.stdin = open('11620.txt')

# def maze(start_i, start_j):

    # global result

    # for k in range(4):
        # new_i = start_i + di[k]
        # new_j = start_j + dj[k]

        # if 0 > new_i or N <= new_i or 0 > new_j or N <= new_j:
            # continue
        # elif int(v[new_i][new_j]) == 0 and visited[new_i][new_j] == 0:
            # visited[new_i][new_j] = 1
            # maze(new_i, new_j)
        # elif int(v[new_i][new_j]) == 3:
            # result = 1
            # return result
    # return result

# T = int(input())

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# for tc in range(1, T+1):
    # N = int(input())
    # v = [list(input()) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    # result = 0

    # for i in range(N):
        # for j in range(N):
            # if int(v[i][j]) == 2:
                # start_i = i
                # start_j = j
                # break
    
    # print(f'#{tc} {maze(start_i, start_j)}')

import sys
sys.stdin = open('1222.txt')

for tc in range(1, 11):
    num = int(input())
    data = input()
    paradox = ''
    st = [0] * 500
    top = -1

    for k in data:
        if k == '+':
            top += 1
            st[top] = k
        elif st[top] == '+':
            while top == 0:
                paradox += k
                paradox += st[top]
                top -= 1
        else:
            paradox += k

    for j in paradox:
        if j != '+':
            top += 1
            st[top] = int(j)
        else: 
            x = st[top]
            top -= 1
            y = st[top]
            st[top] = x + y
    print(f'#{tc} {st[top]}')