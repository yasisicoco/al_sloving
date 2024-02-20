def preorder(N):
    global cnt
    if N:
        cnt += 1
        preorder(left[N])
        preorder(right[N])
    

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    parent = [0] * (E+2)
    for i in range(0, E*2, 2):
        p, c = arr[i], arr[i+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        # parent[c] = p
    # print(left)
    # print(right)

    # c = N # 자식이 루트노드일때
    # while parent[c] != 0: # 자식노드b에 부모가 있다면
    #     c = parent[c]
    # print(parent)
    # root = c

    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')