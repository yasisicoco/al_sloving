# 가운데 터뜨리면 상하좌우가 같이 터짐
# 종이 꽃가루 개수 A가 주어짐.
# 한개의 풍선 선택 -> 날릴수있는 꽃가루의 합 중 최대.

# 전략
# 최댓값 변수설정 / 방향 벡터 설정(상하좌우)
# 포문 돌면서 종이 꽃가루 찾기
# 종이 꽃가루를 찾으면 방향벡터로 돌고, 꽃가루갯수 합더하기

from pprint import pprint
# 방향 벡터설정
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def vec(r, c):
    global sumone

    for k in range(4):
        ni = r + di[k]
        nj = c + dj[k]

        if 0 <= ni < N and 0 <= nj < M:
            sumone += arr[ni][nj]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # N줄

    result = 0 # 초기화
    for i in range(N):
        for j in range(M): # 배열의 가로길이
            sumone = arr[i][j] # 현재장소 꽃가루 개수
            si = i # 상하좌우 확인
            sj = j
            vec(si, sj) # 들어가서 상하좌우 값 더하기
            if result <= sumone:
                result = sumone
    print(f'#{tc} {result}')