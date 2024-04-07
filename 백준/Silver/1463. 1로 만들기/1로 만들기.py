N = int(input())
visi = [0] * (N+1)

for x in range(2, N+1):
    visi[x] = visi[x-1] + 1

    if x % 3 == 0:
        visi[x] = min(visi[x], visi[x//3] + 1)
    if x % 2 == 0:
        visi[x] = min(visi[x], visi[x//2] + 1)

print(visi[N])