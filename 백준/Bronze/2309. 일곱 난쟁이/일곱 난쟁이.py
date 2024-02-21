lst = []
for _ in range(9):
    lst.append(int(input()))


for i in range(9): 
    for j in range(i+1, 9):
        if sum(lst) - (lst[i] + lst[j]) == 100:
            a = lst[i]
            b = lst[j]

lst.sort()
for l in lst:
    if l == a or l == b:
        continue
    print(l)