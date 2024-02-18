max = 0
for i in range(1, 6):
    score = map(int, input().split())
    cnt = i
    result = sum(score)
    if max <= result:
        max = result
        realcnt = cnt
print(f'{realcnt} {max}')
