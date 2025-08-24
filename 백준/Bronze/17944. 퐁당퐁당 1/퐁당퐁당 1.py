import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arms = 2*N
flag = True
arm = 0
for t in range(T):
    if arm < arms and flag:
        arm += 1
    else:
        arm -= 1

    if arm == arms:
        flag = False
    elif arm == 1:
        flag = True
    
print(arm)