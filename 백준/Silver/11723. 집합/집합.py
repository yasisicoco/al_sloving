import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
    char = input().split()
    
    if char[0] == 'add':
        if int(char[1]) in S:
            continue
        else:
            S.append(int(char[1]))
    elif char[0] == 'remove':
        if int(char[1]) not in S:
            continue
        else:
            while int(char[1]) in S:
                S.remove(int(char[1]))
    elif char[0] == 'check':
        if int(char[1]) in S:
            print(1)
        else:
            print(0)
    elif char[0] == 'toggle':
        if int(char[1]) in S:
            while int(char[1]) in S:
                S.remove(int(char[1]))
        else:
            S.append(int(char[1]))
    elif char[0] == 'all':
        S = []
        for i in range(1, 21):
            S.append(i)
    elif char[0] == 'empty':
        S = []
