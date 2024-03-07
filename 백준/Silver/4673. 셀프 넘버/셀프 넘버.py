lst = list(range(1, 10001))

for i in range(1, 10001):
    strnum = str(i)
    sumone = int(strnum)
    for j in strnum:
        sumone += int(j)
    if sumone <= 10000 and sumone in lst:
        lst.remove(sumone)
    
for j in lst:
    print(j)