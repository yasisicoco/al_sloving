import sys
input = sys.stdin.readline

def bt(prev, strLen):
    result = 0

    if strLen == len(S):
        return 1
    
    for i in lucky.keys():
        if i == prev or lucky[i] == 0:
            continue

        lucky[i] -= 1
        result += bt(i, strLen+1)
        lucky[i] += 1
    
    return result


S = input().strip()
lucky = dict()
for s in S:
    if s in lucky:
        lucky[s] += 1
    else:
        lucky[s] = 1

print(bt('', 0))