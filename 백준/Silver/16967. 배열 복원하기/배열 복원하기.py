import sys
input = sys.stdin.readline

# 크기가 H * W 인 배열 A와 두 정수 X,Y
# 크기가 (H + X) * (W + Y) 인 배열 B는 배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐만들 수 있다.
# 수가 겹치면 합쳐짐

h, w, x, y = map(int, input().split())

b=[]
for i in range(h+x):
   ary = list(map(int, input().split()))
   b.append(ary)

a = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i >= x and j >= y:
            a[i][j] = b[i][j] - a[i-x][j-y]
        else:
            a[i][j] = b[i][j]

for i in range(h):
    print(*a[i])