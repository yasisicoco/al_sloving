from sys import stdin; input = stdin.readline

def virus(start, vertex):
    visited = [0] * (vertex + 1)
    stack = []
    visited[start] = 1
    # print(start)
    cnt = 0
    while True:
        for a in adjl[start]:
            if visited[a] == 0:
                visited[a] = 1
                stack.append(start)
                start = a
                # print(start)
                cnt += 1
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
                # return cnt
    return cnt

# V : 컴퓨터 수(노드 수)
V = int(input())
# E : 연결 쌍 수(간선 수)
E = int(input())
# 인접 리스트
adjl = [[] for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u)   # 무향그래프

print(virus(1, V))