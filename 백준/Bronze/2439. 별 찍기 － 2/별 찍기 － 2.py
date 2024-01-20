N = int(input())
a = '*'
if 1 <= N <= 100:
    for i in range(1, N + 1):
        print(f'{i * a}'.rjust(N))