import sys

N, K = map(int, sys.stdin.readline().split())
# N개의 서로 다른 양의 정수, K번 교환
a = list(map(int, sys.stdin.readline().split())) # 배열 A

cnt = 0
result = -1
for i in range(N-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            cnt += 1
            if cnt == K:
                result = f'{a[j]} {a[j+1]}'
print(result)