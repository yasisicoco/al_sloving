import sys
input = sys.stdin.readline

n = int(input())
result = 0
for i in range(n):
    eng = input()
    empty = []
    flag = False
    prev = ''
    for j in eng:
        if prev == j:
            continue
        else:
            if prev == '':
                prev = j
            elif prev != j:
                prev = j

        if j not in empty:
            empty.append(j)
        else:
            flag = True
    
    if flag == False:
        result += 1

print(result)