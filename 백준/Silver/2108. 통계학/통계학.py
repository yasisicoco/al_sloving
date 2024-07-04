from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

# 산술 평균
a = round(sum(arr) / N)

# 중앙값
arr.sort()
b = arr[N//2]

# 최빈값
freq = Counter(arr).most_common()
if len(freq) > 1 and freq[0][1] == freq[1][1]:
    c = freq[1][0]
else:
    c = freq[0][0]

# 범위
d = max(arr) - min(arr)

print(a)
print(b)
print(c)
print(d)