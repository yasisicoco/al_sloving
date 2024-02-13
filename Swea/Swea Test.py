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
#     visited = [0] * (V+1) #visited, stack 생성 및 초기화
#     st = []
#     visited[i] = 1  # 시작점 방문
#     print(i)        # 정점에서 할 일
#     while True: # 탐색
#         # 현재 방문한 정점에 인접하고 방문안한 정점w 있으면
#         for w in adjl[i]:
#             if visited[w] == 0:
#                 st.append(i)    # push(i), i를 지나서
#                 i = w           # w에 방문
#                 visited[i] = 1  # 방문해서 할일
#                 print(i)
#                 break   # for w
#         else:                   # for w, i에 남은 인접 정점이 없으면
#             if st:    # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
#                 i = st.pop()
#             else:   # 스택이 비어있으면 (출발점에서 남은 정점이 없으면)
#                 break   # while True
#     return
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))

# # 인접리스트
# adjl = [[] for _ in range(V+1)] # ardjl[i] 행에 i에 인접인 정점번호
# for i in range(E):
#     n1, n2 = arr[i*2], arr[i*2+1]
#     adjl[n1].append(n2)
#     adjl[n2].append(n1) #방향이 없는 경우
# visited = [0]*(V+1) #visited, stack 생성 및 초기화
# dfs(1, V)






# 소정누나 스택


# T = int(input())
# for tc in range(1, T+1):
    
#     v = [[] for _ in range(V + 1)] # 인접리스트
#     visited = [False for _ in range(V+1)] # 본거
    
#     V, E = map(int, input().split())
#     for i in range(E):
#         a, b = map(int, input().split())
#         v[a].append(b)
#         # v[b].append(a) # 양방향
        
# def dfs(S, G):
    
#     for j in v[S]:
#         if visited[j] == True:
#             continue
#         visited[j] = True
#         # 연산, 조건
#         dfs(j, G)
        
#         if j == G:
#             ans = 1
#             break

# 1219
# import sys
# sys.stdin = open('1219.txt', 'r')

# for tc in range(1, 11):
#     T, E = map(int, input().split())
    
#     v = [[] for _ in range(101)]
#     visited = [False for _ in range(101)]
    
#     lst = list(map(int, input().split()))
#     for i in range(0, E*2, 2):
#         a, b = lst[i], lst[i+1]
#         v[a].append(b) # 유향 그래프
    
#     result = 0
#     def dfs(cur, end):
#         global result
#         for k in v[cur]:
#             if visited[k]:
#                 continue
#             visited[k] == True
#             if k == end:
#                 result = 1
#             cur = k
#             dfs(cur, end)
#         else:
#             return result

#     # dfs(cur, R) 현재 == 0, 도착점 == 99
#     result = dfs(1, 99)
    
#     print(f'#{tc} {result}')


# 11613
# import sys
# sys.stdin = open('11613.txt')

# T = int(input())
# for tc in range(1, T+1):

#     stack = []
#     fx = input().split()

#     result = 'error'
#     for i in fx:
#         if i == '.':
#             if len(stack) == 1:
#                 result = stack.pop()

#         elif i in '*/+-': # 연산자일때
#             if len(stack) < 2:
#                 break
#             a = stack.pop()
#             b = stack.pop()

#             if i == '*':
#                 c = a * b
#                 stack.append(c)
#             elif i == '/':
#                 c = b / a
#                 stack.append(int(c))
#             elif i == '+':
#                 c = a + b
#                 stack.append(c)
#             elif i == '-':
#                 c = b - a
#                 stack.append(c)
        
#         else: # 숫자면
#             stack.append(int(i))
    
#     print(f'#{tc} {result}')
    

# 1222
# import sys
# sys.stdin = open('1222.txt', 'r')
# for tc in range(1, 11):
#     a = int(input()) # 계산식 길이

#     b = input() # 문자열 계산식
#     stack = [0] * a
#     top = -1
#     postfix = []
    
#     for tk in b:
#         if tk == '+':
#             # top += 1 # push
#             stack[top] = tk
#         elif tk != '+':
#             postfix.append(int(tk))
#             if len(postfix) == 2 and '+' in stack:
#                 one = postfix.pop()
#                 two = postfix.pop()
#                 # stack.pop(0)
#                 # top -= 1
#                 someone = one + two
#                 postfix.append(someone)
    
#     result = postfix.pop()

#     print(f'#{tc} {result}')



#11620
# import sys
# sys.stdin = open('11620.txt', 'r')

# T = int(input())
# for tc in range(T+1):
#     N = int(input())
#     v = [list(map(int, input().split())) for _ in range(N)]
#     visited = [False for _ in range(N)]
#     print(v)

#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]

#     for i in range(N):
#         for j in range(N):
#             if v[i][j] == 2:
#                 for k in range(4):
#                     i = i + di[k]
#                     j = j + dj[j]
#                     if 0 <= v[i][j] <= 3:
#                         if v[i][j] == 1:
#                             pass
#                         elif v[i][j] == 0:
#                             i = i + di[k]
#                             j = j + dj[j]

# def back(i, j):
#     for l in v[i][j]:
#         if l == 3:
#             return 1
#         elif l == 1:
#             continue
#         else:
#             continue



import sys
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

def dfs(start, count):
    visited[start] = count

    for i in arr[start]:
        if visited[i] == 0:
            dfs(i, count + 1)
    return

arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u) # 무방향

for s in arr:
    s.sort()

dfs(R, 1)
for n in range(1, N + 1):
    print(visited[n])