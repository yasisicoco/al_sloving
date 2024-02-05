# N :  배열 A의 크기, K : 교환 횟수
N, K = map(int, input().split())
a = list(map(int, input().split()))

def bubble_sort(a, N, K):
    cnt = 0
    res = []
    for last in range(N-1, 0, -1):
        if cnt == K:
            res.append(a[i])
            res.append(a[i + 1])
            break
        for i in range(last):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                cnt += 1
    if len(res) == 0:
        res.append(-1)
    return res

result = bubble_sort(a, N, K)

for r in range(len(result)):
    print(result[r], end=' ')