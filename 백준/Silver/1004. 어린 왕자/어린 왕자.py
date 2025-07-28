T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = list(map(int, input().split()))
    n = int(input())
    cnt =0
    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        dist1 = (x1 - cx)**2 + (y1 - cy)**2
        dist2 = (x2 - cx)**2 + (y2 - cy)**2        
        planet_cr = cr**2
        
        if planet_cr > dist1 and planet_cr > dist2:
            continue
        elif planet_cr > dist1:
            cnt += 1
        elif planet_cr > dist2:
            cnt += 1
            
    print(cnt)