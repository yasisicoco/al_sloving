K = int(input())

lst = []
for i in range(K):
    num = int(input())
    
    if num == 0:
        lst.pop()
        continue
    else:
        lst.append(num)
    # print(lst)

print(sum(lst))