import sys
sys.stdin = open('ladder1.txt')

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    case = [list(map(int, input().split())) for _ in range(100)]
    
    for line in case:
        print(*line)