<<<<<<< HEAD
T = 10
for tc in range(1, T+1):
    leng, num = map(str, input().split())
    leng = int(leng)
    
    st = []
    for i in range(leng): # num의 길이만큼 순회
        # 스택안에 아무것도 없을때, 스택의 맨뒤와 문자열의i번째가 다를때 추가
        if st == [] or st[-1] != num[i]:
            st.append(num[i])
        
        else: # 스택의 맨뒤와 문자열의 i번째가 같을 때
            st.pop() # 스택 후입을 선출시킨다.
    
    # 다 돌고 스택 프린트
    print(f'#{tc}', ''.join(st))
=======
import sys
sys.stdin = open('swea\\input\\1210.txt', 'r')

# 방향 벡터설정
di = [0, 0, 1, -1] # 우 좌 하 상
dj = [1, -1, 0, 0]

def dfs(i, j):

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        # ni, nj 가 배열 안에 있고, 
        if 0 <= ni < 100 and 0 <= nj < 100
            if visited[ni][nj] == True: # 방문했던 곳이면 다음 반복문으로
                continue
            visited[ni][nj] = True # 아니면 방문처리 후
            i, j = ni, nj # 다음 장소로
            dfs(i, j)


T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    visited = [[False] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                si = i
                sj = j
                break # 시작점 찾기
    
    dfs(si, sj)
>>>>>>> 3749e6a7d99a5cb321d9f6b13849cf04cf72bc9e
