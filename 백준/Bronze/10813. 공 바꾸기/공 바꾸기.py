N, M = map(int, input().split())
lst_1 = []
for i in range(1, N+1):
    lst_1.append(i)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lst_1[a], lst_1[b] = lst_1[b], lst_1[a]
    
print(*lst_1)