# 수열 만들기
lst = []
for i in range(1000):
    if len(lst) <= 1000:
        for _ in range(i):
            lst.append(i)
    else:
        break

a, b = map(int, input().split())
print(sum(lst[a-1:b]))