N = int(input())
solve = input()

cnt = 1
mount = False
if solve[0] == 'B':
    for _ in solve:
        if _ == 'R':
            mount = True
            continue
        else:
            if mount:
                cnt += 1
                mount = False
            else:
                continue
        
else:
    for _ in solve:
        if _ == 'B':
            mount = True
            continue
        else:
            if mount:
                cnt += 1
                mount = False
            else:
                continue

if mount:
    cnt += 1
print(cnt)