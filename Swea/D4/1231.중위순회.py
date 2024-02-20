import sys
sys.stdin = open('swea\\input\\1231.txt', 'r')


def inorder(cur, R):
    if cur: # 0 이 아니면
        
        inorder(left[cur], R)
        # int(case[cur][0])
        # print(case[cur][0])
        string.append(case[cur][1])
        inorder(right[cur], R)

for tc in range(1, 11):
    N = int(input()) # 정점수
    E = N-1 # 간선수

    left = [0] * (N+1)
    right = [0] * (N+1)
    P = [0] * (N+1)

    case = [0] * (N+1)
    for i in range(1, N+1):
        case[i] = input().split()
        
    string = []
    arr = []
    for j in range(1, N+1):
        if len(case[j]) == 4:
            arr.append(case[j][0])
            arr.append(case[j][2])
            arr.append(case[j][0])
            arr.append(case[j][3])
        elif len(case[j]) == 3:
            arr.append(case[j][0])
            arr.append(case[j][2])

    for k in range(0, E*2, 2):
        p, c = arr[k], arr[k+1]
        p = int(p)
        c = int(c)
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    # print(left)
    # print(right)
    inorder(1, 1)
    print(f'#{tc}', end=' '); print(*string, sep='')