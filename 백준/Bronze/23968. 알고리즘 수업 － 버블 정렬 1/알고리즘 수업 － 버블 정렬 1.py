N, K = map(int, input().split())
a = list(map(int, input().split()))

def bubble_sort(N, K):
    cnt = 0
    res = []
    for last in range(N-1, 0, -1):
        for i in range(last):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                cnt += 1

            if cnt == K:
                res.append(a[i])
                res.append(a[i + 1])
                return res

    return [-1]

result = bubble_sort(N, K)

for r in range(len(result)):
    print(result[r], end=' ')