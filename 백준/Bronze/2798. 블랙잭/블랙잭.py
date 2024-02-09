N, M = map(int, input().split())
number = list(map(int, input().split()))

max = 0
for i in range(N):
    if i < N-2:
        one = number[i]
        for j in range(N):
            if i < j < N-1:
                two = number[j]
                for k in range(N):
                    result = max
                    if j < k:
                        thr = number[k]
                        max = number[i] + number[j] + number[k]
                        if max <= M and max > result:
                            result = max
                        else:
                            max = result
print(result)