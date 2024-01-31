import sys
sys.stdin = open('color.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)] # 테스트 케이스 배열 초기화
    # for line in arr:
    #     print(*line)
    N = int(input())
    lst = []
    for _ in range(N):
        r1, c1, r2, c2, rgb = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if arr[r][c] == 0:  # rgb가 0일 때
                    arr[r][c] = rgb # 색칠하기
                elif arr[r][c] == 1: # rgb가 1일 때
                    if rgb == 1:
                        pass
                    elif rgb == 2:
                        arr[r][c] += rgb  # 색칠하기
                elif arr[r][c] == 2:
                    if rgb == 1:
                        arr[r][c] += rgb
                    elif rgb == 2:
                        pass  # 색칠하기

        result = 0
        for line in arr:
            result += line.count(3)

    print(f'#{tc} {result}')
    #     print()
    # print()



