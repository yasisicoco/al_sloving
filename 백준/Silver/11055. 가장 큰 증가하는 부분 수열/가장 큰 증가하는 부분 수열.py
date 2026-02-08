A = int(input())
arr = list(map(int, input().split()))

udp = arr[:]
for i in range(A):
    for j in range(i):
        if arr[j] < arr[i]:
            udp[i] = max(udp[i], udp[j] + arr[i])

print(max(udp))
