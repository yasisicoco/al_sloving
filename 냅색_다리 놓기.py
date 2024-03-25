def bridge(num, sumone, k):
    global result, max_bridge
    if num == N:
        if sumone <= V:
            if k == max_bridge:
                result = min(sumone, result)
            result = max(sumone, result)
            max_bridge = max(k, max_bridge)
            return
        return

    bridge(num + 1, sumone, k)
    bridge(num + 1, sumone + C[num], k + 1)


T = int(input())
for tc in range(1, T+1):
    # N: 섬의수 V: 건설비용
    N, V = map(int, input().split())

    # 건설비용
    C = list(map(int, input().split()))
    # 51
    max_bridge = 0
    result = 0
    bridge(0, 0, 0)
    print(f'#{tc} {max_bridge} {result}')