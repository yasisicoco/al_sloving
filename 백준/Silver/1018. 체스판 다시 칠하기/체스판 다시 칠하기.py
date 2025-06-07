import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        tmp1 = 0
        tmp2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0: # 짝수일때
                    if board[a][b] != 'W': # 흰색아니면
                        tmp1 += 1
                    else: # 검은색아니면
                        tmp2 += 1
                else: # 홀수일때
                    if board[a][b] != 'B': # 검은색아니면
                        tmp1 += 1
                    else: # 흰색아니면
                        tmp2 += 1
        
        result.append(tmp1)
        result.append(tmp2)

print(min(result))