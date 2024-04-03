def readbook(idx, dy, pg):
    global page
    if dy <= N:
        page = max(pg, page)

    if dy > N:
        return
    if idx >= M:
        return
    
    readbook(idx + 1, dy + lst[idx][0], pg + lst[idx][1])
    readbook(idx + 1, dy, pg)

# 남은기간N, 챕터의 수M
N, M = map(int, input().split())
lst = []
for _ in range(M):
    d, p = map(int, input().split())
    lst.append([d, p])

page = 0
readbook(0, 0, 0)
print(page)