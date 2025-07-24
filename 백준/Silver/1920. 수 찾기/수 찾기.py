import sys
input = sys.stdin.readline

N = int(input())
one = list(map(int, input().split()))
one.sort()
M = int(input())
two = list(map(int, input().split()))

result = []
for t in two:
    s = 0
    e = N - 1
    flag = False
    while s <= e:
        mid = (s+e) // 2
        if t == one[mid]:
            result.append(1)
            flag =True
            break
        elif t < one[mid]:
            e = mid - 1
        else:
            s = mid + 1
    if flag == False:
        result.append(0)

for i in result:
    print(i)