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

# s = set([color_1, color_2, color_3, color_4])
# lst = list(s)
# lst.sort()

# for i in lst:
#     for j in lst:
#         print(i, j)

# 1110.더하기사이클

num = int(input()) #68
first_num = num
cnt = 0

while True:
    a = num % 10 # 8
    b = num // 10 # 6
    num = (a * 10) + ((a + b) % 10)
    cnt += 1
    if num == first_num:
        break
print(cnt)