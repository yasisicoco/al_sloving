import sys
sys.stdin = open('1222.txt', 'r')

# state 1
# for tc in range(1, 11):
#     num = int(input())
#     data = input()
#     paradox = ''
#     st = [0] * 500
#     top = -1
 
#     for k in data:
#         if k == '+':
#             top += 1
#             st[top] = k
#         elif st[top] == '+':
#             while top == 0:
#                 paradox += k
#                 paradox += st[top]
#                 top -= 1
#         else:
#             paradox += k
 
#     for j in paradox:
#         if j != '+':
#             top += 1
#             st[top] = int(j)
#         else: 
#             x = st[top]
#             top -= 1
#             y = st[top]
#             st[top] = x + y
#     print(f'#{tc} {st[top]}')


# state 2
for tc in range(1, 11):
    
    # 문자열계산식 길이
    length = int(input())
    # 문자열
    strlst = input()
    # 스택
    st = [0] * 500
    # 숫자넣을 문자열
    numlst = ''
    # 탑
    top = -1
    
    for i in strlst:
        if i == '+':
            top += 1
            st[top] = i
        elif st[top] == '+':
            while top == 0:
                numlst += i
                numlst += st[top]
                top -= 1
        else:
            numlst += i
    # print(numlst)
    for j in numlst:
        if j != '+':
            top += 1
            st[top] = int(j)
        else:
            x = st[top]
            top -= 1
            y = st[top]
            st[top] = x + y
    print(f'#{tc} {st[top]}')