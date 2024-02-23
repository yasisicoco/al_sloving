key = 1004

def lock(num):
    return num ^ key

print(lock(1000))
print(lock(4))

t = 1
for i in range(5):
    print(bin(t), t)
    t = t << 1

T = int(input())

for tc in range(1, T+1):
    for _ in range(5):
        N, M = map(int, input().split())
        if not bin(M) == 0:
            print(f'#{tc} ON')
        else:
            print(f'#{tc} OFF')



M = 31
N = 5
def Test():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return False
        tar = tar >> 1
    return True
print(Test())

num = 0.1
print(f'{num:.20f}')