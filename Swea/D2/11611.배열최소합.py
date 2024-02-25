# state1
import sys
# sys.stdin = open('C:\\Users\\지누잉\\Desktop\\jinwoo\\al_sloving\\Swea\\input\\11611.txt')
sys.stdin = open('./Swea/input/11611.txt')
    
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


# state2
# def dfs(n, sumone):
#     global result

#     if n == N: # 행을 다 돌았을 때 n == 3 (배열을 넘어가면)
#         if result >= sumone: # 결과보다 sumone이 작으면
#             result = sumone
#             return
    
#     if result <= sumone: # 세개 더하기도 전에 최소값을 넘어가면
#         return

#     for j in range(N): # 배열 순회
#         if visited[j] == False: # 첫방문이면
#             visited[j] = True # 방문처리
#             dfs(n+1, sumone+arr[n][j]) # 다음 행으로 더한값을 가져간다
#             visited[j] = False # 순회끝나면 다음 순열을 위해 방문취소처리



# T = int(input())
# for tc in range(1, T+1): 
#     N = int(input()) # 3 <= N < 10
#     # NxN 배열
#     arr = [list(map(int, input().split())) for _ in range(N)]   # N개의 리스트
#     # 방문처리 (중복방지용)
#     visited = [False for _ in range(N)]

#     # 최소값 구하기
#     result = N * 100
#     dfs(0, 0) # 행 = 0 부터, sumone = 0부터 더할것임
#     print(f'#{tc} {result}')
