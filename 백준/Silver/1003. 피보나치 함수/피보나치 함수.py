def fibo(n):
    memo_zero = [-1] * (n + 1)
    memo_one = [-1] * (n + 1)

    memo_zero[0] = 1
    memo_one[0] = 0
    if n >= 1: 
        memo_zero[1] = 0
        memo_one[1] = 1

    for i in range(2, n + 1):
        memo_zero[i] = memo_zero[i - 1] + memo_zero[i - 2]
        memo_one[i] = memo_one[i - 1] + memo_one[i - 2]

    print(memo_zero[n], memo_one[n])

T = int(input())
for _ in range(T):
    N = int(input())
    fibo(N)