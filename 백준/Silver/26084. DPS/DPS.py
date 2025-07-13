import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

S = input().strip()
N = int(input())
lst = [input().strip()[0] for _ in range(N)]
ans = 0

need = {}
for c in S:
    if c in need:
        need[c] += 1
    else:
        need[c] = 1

words = {}
for word in lst:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

def comb(n, k):
    if k > n:
        return 0
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k+1):
        result = result * (n-k+i) // i
    return result

ans = 1
for c, cnt in need.items():
    ans *= comb(words.get(c, 0), cnt)

print(ans)

'''2 / 24
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

S = input().strip()
N = int(input())
lst = [input().strip() for _ in range(N)]
ans = 0
def dfs(cur, s):
    global ans

    if len(cur) == len(S):
        temp = ''.join(cur)
        if temp == S:
            ans += 1
        return

    for i in range(s, N):
        cur.append(lst[i][0])
        dfs(cur, i+1)
        cur.pop()

dfs([], 0)
print(ans)
'''

'''1 / 4
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

S = input().strip()
N = int(input())
lst = [input().strip() for _ in range(N)]
ans = 0
visited = [False] * N
def dfs(cur, visited):
    global ans

    if len(cur) == len(S):
        temp = ''.join(cur)
        if temp == S:
            ans += 1
        return

    for i in range(N):
        if visited[i]:
            continue
        cur.append(lst[i][0])
        visited[i] = True
        dfs(cur, visited)
        visited[i] = False
        cur.pop()

dfs([], visited)
print(ans)
'''