dir = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}


eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num = ['8', '7', '6', '5', '4', '3', '2', '1']
chess = []
for i in range(8):
    arr = []
    for j in range(8):
        dup = eng[j]+num[i]
        arr.append(dup)
    chess.append(arr)

from collections import deque
def game():
    global sr, sc, gr, gc
    q = deque(move)
    
    while q:
        ci, cj = q.popleft()
        k_ni = sr + ci
        k_nj = sc + cj
        if 0 <= k_ni < 8 and 0 <= k_nj < 8:
            sr, sc = k_ni, k_nj
            if k_ni == gr and k_nj == gc:
                s_ni = gr + ci
                s_nj = gc + cj
                if  0 <= s_ni < 8 and 0 <= s_nj < 8:
                    gr, gc = s_ni, s_nj
                else:
                    sr -= ci
                    sc -= cj
                

king, stone, N = input().split()
N = int(N)


move = []
for _ in range(N):
    move.append(dir[input()])
    
    
sr=0; sc=0; gr=0; gc=0
for i in range(8):
    for j in range(8):
        if chess[i][j] == king:
            sr, sc = i, j
        if chess[i][j] == stone:
            gr, gc = i, j

game()
print(chess[sr][sc])
print(chess[gr][gc])