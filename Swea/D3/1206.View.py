tc = 10
for tci in range(1, tc+1):
    N = int(input())
    high = list(map(int, input().split()))
    view = 0
    for i in range(2, N-1): # len(high)+2 : len(high)-2
        lst = []
        if high[i] - high[i-1] > 0 and high[i] - high[i-2] > 0:
            if high[i] - high[i+1] > 0 and high[i] - high[i+2] > 0:
                lst = [high[i+1], high[i+2], high[i-1], high[i-2]]
                lst.sort()
                view += high[i] - lst[-1]
    print(f'#{tci} {view}')
