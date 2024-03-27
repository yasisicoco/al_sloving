def inorder(s, e, depth):
    if s == e:
        st[depth].append(build[s])
        return
    
    root = (s + e) // 2 # 중앙값이 루트값
    st[depth].append(build[root])
    inorder(s, root-1, depth+1) # 이분탐색?
    inorder(root+1, e, depth+1)

K = int(input())
build = list(map(int, input().split()))
st = [[] for _ in range(K)] # 레벨크기만큼 리스트를 만들고 레벨에 각각 넣어줄 예정

inorder(0, len(build)-1, 0) # 인덱스값으로 넣을거라 -1
for i in st:
    for ans in i:
        print(ans, end=" ")
    print()