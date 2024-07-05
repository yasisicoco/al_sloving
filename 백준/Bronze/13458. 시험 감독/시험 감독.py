import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(N):
    arr[i] -= B
    cnt += 1
    if arr[i] <= 0:
        continue
    else:
        if arr[i] % C == 0:
            num = arr[i] // C
            cnt += num
        else:
            num = arr[i] // C
            cnt += (num + 1)
print(cnt)