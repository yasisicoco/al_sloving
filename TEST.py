# N :  배열 A의 크기, K : 교환 횟수
# N, K = map(int, input().split())
# a = list(map(int, input().split()))
# 
# def bubble_sort(a, N, K):
    # cnt = 0
    # res = []
    # for last in range(N-1, 0, -1):
        # if cnt == K:
            # res.append(a[i])
            # res.append(a[i + 1])
            # break
        # for i in range(last):
            # if a[i] > a[i+1]:
                # a[i], a[i+1] = a[i+1], a[i]
                # cnt += 1
    # if len(res) == 0:
        # res.append(-1)
    # return res
# 
# result = bubble_sort(a, N, K)
# 
# for r in range(len(result)):
    # print(result[r], end=' ')




# 28445. 알록달록 앵무새
# color_1, color_2 = input().split()
# color_3, color_4 = input().split()
#
# s = set([color_1, color_2, color_3, color_4])
# lst = list(s)
# lst.sort()
#
# for i in lst:
#     for j in lst:
#         print(i, j)


# SSSSSSSSSStack
# def push(n):
#     global top
#     top += 1
#     if top==size:
#         ptint('Overflow!')
#     else:
#         stack[top] = n
# top = -1
# size = 10
# stack = [0] * size # 최대 10개 push
#
# top += 1 # push(10)
# stack[top] = 10
#
# top += 1
# stack[top] = 20 # push(20)
#
# push(30)
#
# while top >= 0:
#     top -= 1
#     print(stack[top+1])

# def fibo(n):
#     global cnt
#     cnt += 1
#     if n<2:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# def fibo_memo(n):
#     global cnt
#     cnt += 1
#     if n!=0 and memo[n]==0:
#         memo[n] = fibo_memo(n-1)+fibo_memo(n-2)
#     return memo[n]
#
# cnt = 0
# n = 7
# print(fibo(n), cnt)
# memo = [0]*(n+1)
# memo[0] = 0
# memo[1] = 1
# print(fibo_memo(n), cnt)

