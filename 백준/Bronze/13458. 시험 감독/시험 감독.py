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
        num = arr[i] // C
        if arr[i] % C == 0:
            cnt += num
        else:
            cnt += (num + 1)
            
print(cnt)