'''
'''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i, V): # 시작 i, 마지막 V
    visited = [0] * (V+1) #visited, stack 생성 및 초기화
    st = []
    visited[i] = 1  # 시작점 방문
    print(i)        # 정점에서 할 일
    while True: # 탐색
        # 현재 방문한 정점에 인접하고 방문안한 정점w 있으면
        for w in adjl[i]:
            if visited[w] == 0:
                st.append(i)    # push(i), i를 지나서
                i = w           # w에 방문
                visited[i] = 1  # 방문해서 할일
                print(i)
                break   # for w
        else:                   # for w, i에 남은 인접 정점이 없으면
            if st:    # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
                i = st.pop()
            else:   # 스택이 비어있으면 (출발점에서 남은 정점이 없으면)
                break   # while True
    return
V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # ardjl[i] 행에 i에 인접인 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) #방향이 없는 경우
visited = [0]*(V+1) #visited, stack 생성 및 초기화
dfs(1, V)




def dfs(i): # 시작 i, 마지막 V
    visited[i] = 1  # 방문표시
    print(i)        # 출력
    # i에 인접하고 방문안한 w가 있으면
    for w in adjl[i]:
        if visited[w]==0:
            dfs(w)
'''
# 정종윤 강사님
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# V (vertex) : 정점수, E (edge) : 간선 수 
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# # 인접리스트로 저장
# # 정점 번호가 1번부터 V번까지이므로: V+1
# G = [[] for _ in range(V + 1)]
# for i in range(0, E*2, 2):
#     u, v = arr[i], arr[i+1]
#     G[u].append(v) # 유향 그래프이면 이것만
#     G[v].append(u) # 무향 그래프이기에 두쪽 다 추가

# for i in range(1, V+1):
<<<<<<< HEAD
#     print(i, '-->', G[i])
=======
#     print(i, '-->', G[i])

'''
fx = (6+5*(2-8)/2)
'''
# stack = []

# top = -1
# stack = [0]*100

# icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖에서 우선순위
# isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서 우선순위

# fx = '(6+5*(2-8)/2)'
# postfix = ''
# for tk in fx:
#     if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]): # 여는 괄호 push, top원소보다 우선순위가 높으면 push
#         top += 1 # push
#         stack[top] = tk
#     elif tk in '*/+-' and isp[stack[top]] >= icp[tk]: # 연산자이고 top원소보다 우선순위가 높지않으면
#         while isp[stack[top]] >= icp[tk]:             # top원소보다 우선순위가 낮을 때까지 pop
#             top -= 1                                  # pop
#             postfix += stack[top+1]
#         top += 1
#         stack[top] = tk
#     elif tk == ')':                                   # 닫는 괄호면, 여는 괄호를 만날때까지 pop
#         while stack[top] != '(':
#             top -= 1
#             postfix += stack[top+1]
#         top -= 1                                      # 여는 괄호 pop 해서 버림
#     else:                                             # 피연산자인 경우
#         postfix += tk

# print(postfix)


# def f(i, k, s, t): # k개의 원소를 가진 배열 A, 부분집합의 합이 t인 경우
#     global cnt
#     cnt += 1
#     if s == t: # 모든 원소에 대해 결정하면
#         for j in range(k):
#             if bit[j]:
#                 print(A[j], end=' ')
#         print()
#     elif i==k: # 모든 원소 고려했으나 s != t
#         return
#     elif s > t: # 고려한 원소의 합이 t보다 큰 경우
#         return
#     else:
#         bit[i] = 1
#         f(i+1, k, s+A[i], t)
#         bit[i] = 0
#         f(i+1, k, s, t)

# N = 10
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bit = [0] * N # [0, 0, 0]
# cnt = 0
# f(0, N, 0, 10)
# print(f'cnt :', cnt)


# def f(i, k, s):
#     global min_v
#     global cnt
#     cnt += 1
#     if i == k:
#         # print(*P)
#         s = 0   # 선택한 원소의 합
#         for j in range(k):  # j행에 대해
#             s += arr[j][P[j]]   # j행에서 P[j]열을 고른 경우의 합 구하기
#         if min_v > s:
#             min_v = s
#     elif s >= min_v:  # 가지치기
#         return
#     else:
#         for j in range(1, k):  # P[i]자리에 올 원소 P[j]
#             P[i], P[j] = P[j], P[i]    # P[i] <-> P[j]
#             f(i+1, k, s+arr[i][P[i]])
#             P[i], P[j] = P[j], P[i]    # 교환 전으로 복구


            
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# P = [i for i in range(N)]
# min_v = 100
# cnt = 0
# f(0, N, 0)
# print(min_v, cnt)

>>>>>>> 09959a84586d67c04e45c5a68871b387367a31ff
