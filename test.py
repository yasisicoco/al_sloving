N, K, T = map(int, input().split())
sharks = list(map(int, input().split()))
sharks.sort()

st = []
q = []
for _ in range(K):
    for shark in sharks:
        if T > shark:
            st.append(shark)    
        else:
            q.append(shark)


    if not st:
        print(T)
        exit()
    feed = st.pop()
    T += feed

    for i in q:
        if i < feed:
            st.append(i)

print(T)