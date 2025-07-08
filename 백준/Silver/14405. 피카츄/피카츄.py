import sys
input = sys.stdin.readline

S = input().strip()

S = S.replace('pi', ' ')
S = S.replace('ka', ' ')
S = S.replace('chu', ' ')
    
if S.strip():
    print('NO')
else:
    print('YES')
