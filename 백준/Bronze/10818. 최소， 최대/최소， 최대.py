N = int(input())
lst = list(map(int, input().split()))
maxlst = lst[0]
minlst = lst[0]

for i in lst[:]:
    if i > maxlst:
        maxlst = i
    elif i < minlst:
        minlst = i
print(minlst, maxlst)