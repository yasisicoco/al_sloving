import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
performance = B//A
warboy_performance = 3 * performance
result = warboy_performance * C

print(result)