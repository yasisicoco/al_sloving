import sys
input = sys.stdin.readline

n = int(input())
big = []
result = []
for _ in range(n):
    big.append(list(map(int, input().split())))

for man1 in big:
    check = 1

    for man2 in big:
        if man1[0]== man2[0] and man1[1] == man2[1]:
            continue
        if man1[0] < man2[0] and man1[1] < man2[1]: # 덩치큰사람이 있다면
            check += 1

    result.append(check)
print(*result)