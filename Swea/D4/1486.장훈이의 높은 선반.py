def dfs(cnt, sum_height):
    global ans
    # 1. 키의 합이 B 이상이면 종료 (sum_height)
    # 2. 모든 점원이 탑을 쌓았다면 종료 (cnt)
    if sum_height >= B:
        ans = min(ans, sum_height)
        return
    if cnt == N:
        return
    
    # 쌓는다
    dfs(cnt + 1, sum_height + arr[cnt])
    # 안쌓는다
    dfs(cnt + 1, sum_height)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 1e9

    dfs(0, 0)
    print(f'#{tc} {abs(ans-B)}')