# def postorder(c):
#     if c != 0:
#         return c
#
#     postorder(c)
#     postorder(c)
#     if c == '/*-+':
#         if c == '/':
#
#         elif c == '*':
#
#         elif c == '-':
#
#         elif c == '+':
#
#     else: # 숫자일 때
#         if num == 0:
#             num = c
#         num2 = c


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N+1):
        p = input().split()     # 문자열을 공백없이 받음 0123
        if len(p) > 3:          # 문자열 p의 길이가 3보다 길면 연산자있음
            tree[i] = p[1]      # 연산자는 해당 노드에 넣기, 2, 3번 자리는 왼,오
            left[i] = p[2]
            right[i] = p[3]
        else:
            tree[i] = int(p[1])

    print(tree)
    print(left)
    print(right)
    # print(f'#{tc} {}')