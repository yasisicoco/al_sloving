import sys
sys.stdin = open('swea\\input\\12919.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    emp = ''
    i = 1
    while N:
        under = 2**(-i)  # 리스트 under에 2의 -1승부터 차례대로 저장

        if N >= under:
            N = N - under
            emp += '1'
        elif under > N > 0:
            emp += '0'
        if len(emp) >= 13:
            emp = 'overflow'
            break
        i += 1
    print(f'#{tc} {emp}')