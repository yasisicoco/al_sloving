from heapq import heappop, heappush

# 시험은 24 x N 시간 후, 과목수 M
N, M = map(int, input().split())
time = N * 24
# 기본점수
base = list(map(int, input().split()))
up = list(map(int, input().split()))
heap = []

for i in range(M):
    if base[i] + up[i] > 100:
        up[i] = 100 - base[i]
    heappush(heap, [-up[i], base[i]])
    print(heap)


studytime = 0
while studytime < time:
    r, c = heappop(heap)
    c -= r
    if c - r > 100:
        r = c - 100
    heappush(heap, [r, c])
    studytime += 1

result = 0
for i in range(M):
    result += heap[i][1]
print(result)