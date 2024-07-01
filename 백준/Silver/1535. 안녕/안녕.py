def back(cnt, h, hap):
    global maxHappy
    
    if h > 0:
        maxHappy = max(hap, maxHappy)
    if cnt == N:
        return
        
    back(cnt+1, h-lose[cnt], hap+get[cnt])
    back(cnt+1, h, hap)

N = int(input())
lose = list(map(int, input().split()))
get = list(map(int, input().split()))

hp = 100
maxHappy = 0

back(0, hp, 0)
print(maxHappy)