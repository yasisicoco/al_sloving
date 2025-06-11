import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
for num in range(2, N+1):
    lst.append(num)
visit = [False] * (N+1)
cnt = 0
for P in range(2, N+1): #2
    if not visit[P]:
        for j in range(P, N+1, P):
            if not visit[j]:
                visit[j] = True #3
                cnt += 1
                if cnt == K:
                    print(j)
                    exit()