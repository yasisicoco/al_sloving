T = int(input())


for i in range(1, T + 1):
    a, b = map(int, input().split())
    result = a + b
    print(f'Case #{i}: {result}')