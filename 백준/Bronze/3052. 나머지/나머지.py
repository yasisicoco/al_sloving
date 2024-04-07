st = set()

for _ in range(10):
    k = int(input())
    l = k % 42
    st.add(l)


print(len(st))