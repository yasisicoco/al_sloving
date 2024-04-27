N1, N2 = map(int, input().split())
ant1 = list(input()) # ABC
ant2 = list(input()) # DEF
T = int(input())

ant = ant1[::-1] + ant2
for _ in range(T):
    for i in range(len(ant)-1):
        if (ant[i] in ant1) and (ant[i+1] in ant2):
            ant[i], ant[i+1] = ant[i+1], ant[i]
            if ant[i+1] in ant1[0]:
                break
print(*ant, sep='')