import sys
input = sys.stdin.readline

n = list(map(int, str(input().strip())))
newN = []
for i in n:
    if i == 9:
        newN.append(6)
    else:
        newN.append(i)
buyCnt = 0
while newN:
    buyCnt += 1
    numSet = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8]
    for num in numSet:
        if num in newN:
            newN.remove(num)

print(buyCnt)
