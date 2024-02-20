A, B = input().split()
N = len(A)
M = len(B)

same = []
for k in A:
    if k in B:
        same = k
        break

cntA = -1
for j in A:
    cntA += 1
    if same == j:
        break

cntB = -1
for l in B:
    cntB += 1
    if same == l:
        break

arr = [['.'] * N for _ in range(M)]

for z in range(M):
    arr[z][cntA] = B[z]
for x in range(N):
    arr[cntB][x] = A[x]

for line in arr:
    print(*line, sep='')