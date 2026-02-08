A = int(input())
arr = list(map(int, input().split()))

udp = [1] * A
for i in range(A):
    for j in range(i):
        if arr[j] < arr[i]:
            udp[i] = max(udp[i], udp[j] + 1)

ddp = [1] * A
for i in range(A-1, -1, -1):
    for j in range(A-1, i, -1):
        if arr[j] < arr[i]:
            ddp[i] = max(ddp[i], ddp[j] + 1)

ans = 0
for i in range(A):
    ans = max(ans, udp[i] + ddp[i] -1)

print(ans)