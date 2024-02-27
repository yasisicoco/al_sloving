    # path[0] : 회사
        # 중간에 고객 2, 3, 4, 5, ..., N+1
    # path[1] : 집

def gohome(x, y, leng):
    global ans

    if x == path[1][0] and y == path[1][1]: # 집의 좌표
        print(ans)
        return
    

    for r in range(2, N+1): # 고객의 집 동선 k : 2 부터
        nx = abs(x - path[r][0]) # 이전에 있던 곳 - 지금 온 곳
        ny = abs(y - path[r][1])
        result = abs(nx - ny) # 거리값

        if leng >= result:
            leng = result
            ans += leng
            break
        gohome(nx, ny, leng)
    






T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    arr = list(map(int, input().split()))
    path = []
    for i in range(0, (N+2)*2, 2):
        a, b = arr[i], arr[i+1]
        path.append((a, b))
    
    ans = 0
    gohome(path[0][0], path[0][1], 0) # 회사의 x좌표, y좌표, 최소값

    

