import sys
input = sys.stdin.readline

n = int(input())
val = list(input().strip())
result = 0

for _ in range(n-1):
    oldVal = val[:]
    newVal = input().strip()
    cnt = 0

    for new in newVal:
        if new in oldVal:
            oldVal.remove(new)
        else:
            cnt += 1
    
    if cnt < 2 and len(oldVal) < 2: # 단어갯수차이
        result += 1

print(result)