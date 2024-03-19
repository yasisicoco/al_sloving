# N * N 체스판에 N 개의 퀸을 전부 두고
# 공격하지 못하는지 확인
# 못하면 +1 , 하면 탐색

def chess(dep): # dep: 퀸의 수, case: 경우의 수
    global case

    if dep == N: # 퀸을 다 두었을 때
        case += 1
        return

    else:
        for i in range(N):
            if visited[i]:
                continue
            a = dep + i
            b = dep - i + (N - 1)
            if line1[a] or line2[b]: # 대각에 있으면
                continue
            visited[i] = line1[a] = line2[b] = 1
            chess(dep + 1) # 같은 행,열에 어차피 못둠
            visited[i] = line1[a] = line2[b] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0] * N
    line1 = [0] * (N + N)
    line2 = [0] * (N + N)
    case = 0
    chess(0)
    print(f'#{tc} {case}')