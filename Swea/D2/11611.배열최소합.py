import sys
sys.stdin = open('C:\\Users\\지누잉\\Desktop\\jinwoo\\al_sloving\\Swea\\input\\11611.txt')
    
def back(i, N, sumone):
    
    global decoy
    
    if i == N:
        if decoy > sumone:
            decoy = sumone
        return
    if decoy <= sumone:
        return
    
    for j in range(i, N):
        visited[i], visited[j] = visited[j], visited[i]
        back(i + 1, N, sumone + arr[i][visited[i]])
        visited[i], visited[j] = visited[j], visited[i]
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [i for i in range(N)]
    decoy = 100
    
    back(0, N, 0)
    print(f'#{tc} {decoy}')