import sys
sys.stdin = open('between_paris.txt')

T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    result = (D / (A+B)) * F # 파리는 A와 B가 부딪힐 때 까지 이동한다.
    print(f'#{tc} {result}')