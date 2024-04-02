N, M = map(int, input().split())

# 바구니
st = [0] * N 

# 공 넣기
for _ in range(M):
    i, j, k = map(int, input().split())
    st[i-1:j] = [k] * (j+1-i)

print(*st)