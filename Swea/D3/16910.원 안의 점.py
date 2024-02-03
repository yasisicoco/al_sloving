import sys
sys.stdin = open('intocircle.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N은 반지름
    center = N + 1 // 2