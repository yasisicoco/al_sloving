import sys
input = sys.stdin.readline

def back(cur):
    if len(cur) == M:
        newCur = sorted(cur)
        temp.add(tuple(newCur))
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] =True
        cur.append(lst[i])
        back(cur)
        cur.pop()
        visited[i] = False

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * N

temp = set()
back([])
result = []
for tem in temp:
    result.append(tem)

result.sort()
for res in result:
    print(*res)