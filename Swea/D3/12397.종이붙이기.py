T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N // 10
    def square(n):
        if n == 1:
            return 1
        elif n == 2:
            return 3

        return square(n-1) + (square(n-2) * 2)

    print(f'#{tc} {square(n)}')