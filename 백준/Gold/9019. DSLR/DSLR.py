from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    n = n * 2
    if n >= 10000:
        n = n % 10000
    return n

def S(n):
    n = n - 1
    if n == -1:
        n = 9999
    return n

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

def bfs(a, b):
    
    q = deque()
    q.append([a, ''])
    while q:
        nn, ss = q.popleft()
        for operation, op_name in zip([D, S, L, R], ['D', 'S', 'L', 'R']):
            result = operation(nn)
            if result == b:
                print(ss + op_name)
                return
            
            if visited[int(result)] == 0:
                visited[int(result)] = 1
                q.append([result, ss+op_name])
            
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    visited[A] = 1
    bfs(A, B)
