T = 10
for tc in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))
 
    high = 0
    low = 101
    high_idx = 0
    low_idx = 0
 
 
    for i in range(len(box)):
        if high < box[i]:
            high = box[i]
            high_idx = i
        if low > box[i]:
            low = box[i]
            low_idx = i
    for _ in range(dump):
        box[high_idx] -= 1
        box[low_idx] += 1
        if box[high_idx] == box[low_idx] or box[high_idx] == box[low_idx] + 1:
            break
        else:
            high = max(box)
            low = min(box)
            high_idx = box.index(high)
            low_idx = box.index(low)
    print(f'#{tc} {box[high_idx] - box[low_idx]}')