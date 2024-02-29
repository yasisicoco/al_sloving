T = int(input())
for tc in range(1, T+1):
    num, A = input().split()
    num = int(num)

    for i in A:
        print(i*num, end='')
    print()