import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().strip()

i, j = 0, 0
result = 0

for count in range(min(n, k)):
    for ch in s:
        if ch == 'U':
            i += 1
        elif ch == 'D':
            i -= 1
        elif ch == 'R':
            j += 1
        else:
            j -= 1
        
        if i == 0 and j == 0:
            result = 1
            break
    if result:
        break

print("YES" if result else "NO")
