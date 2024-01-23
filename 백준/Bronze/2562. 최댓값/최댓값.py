K = 9
tc = 0
lst = [0]
for num in range(1, K+1):
    N = int(input())
    if N > lst[0]:
        lst[0] = N
        tc = num
print(lst[0])
print(tc)