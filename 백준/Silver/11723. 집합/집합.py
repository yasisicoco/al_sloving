import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    char = input().split()
    
    if char[0] == 'add':
        S.add(int(char[1]))
    elif char[0] == 'remove':
        S.discard(int(char[1]))
    elif char[0] == 'check':
        print(1 if int(char[1]) in S else 0)
    elif char[0] == 'toggle':
        if int(char[1]) in S:
            S.discard(int(char[1]))
        else:
            S.add(int(char[1]))
    elif char[0] == 'all':
        S = set(range(1, 21))
    elif char[0] == 'empty':
        S = set()
