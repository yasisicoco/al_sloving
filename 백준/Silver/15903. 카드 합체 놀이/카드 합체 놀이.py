import heapq

N, M = map(int, input().split())
card = list(map(int, input().split()))

heapq.heapify(card)

for _ in range(M):
    min1 = heapq.heappop(card)
    min2 = heapq.heappop(card)

    sumMin = min1 + min2
    for _ in range(2):
        heapq.heappush(card, sumMin)

print(sum(card))