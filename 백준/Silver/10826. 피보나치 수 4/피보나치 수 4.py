N = int(input())

if N == 0:
    print(0)
else:
    fn = [0] * (N+1)
    fn[1] = 1
    for i in range(2, N+1):
        fn[i] = fn[i-1] + fn[i-2]
    print(fn[N])