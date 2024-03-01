def recur():
    if len(st) == M:
        print(*st)
        return

    for i in range(1, N+1):
        st.append(i)
        recur()
        st.pop()

N, M = map(int, input().split())
st = []
recur()