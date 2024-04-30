N, M = map(int, input().split())
nolook_nolisten = []
no_look = set()

for i in range(N):
    no_look.add(input())
for i in range(M):
    no_listen = input()
    if no_listen in no_look:
        nolook_nolisten.append(no_listen)
        no_look.remove(no_listen)

nolook_nolisten.sort()
print(len(nolook_nolisten))
for people in nolook_nolisten:
    print(people)