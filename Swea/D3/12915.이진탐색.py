T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 완전 이진트리 노드수, 마지막 노드 번호

    root = []
    idx = 0
    def inorder(cur):
        global idx
        if cur > N:
            return
        
        inorder(cur * 2)
        idx += 1
        root.append([cur, idx])
        inorder(cur * 2 + 1)

    inorder(1)
    # 루트 = 순서첫번째, 인덱스 = 순서/N
    for u in root:
        if u[0] == N//2:
            result = u[1]
        if u[0] == 1:
            realroot = u[1]
    print(f'#{tc}', end=' '); print(realroot, end=' '); print(result)
    # print(f'#{tc}', end=' ')
    # print(sorted(root)[0][1], sorted(root)[N // 2 - 1][1])