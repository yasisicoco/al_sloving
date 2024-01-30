import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # K = 이동거리 , N = 정류장 수 , M = 충전기 설치 정류장 수
    charge = list(map(int, input().split())) # 충전기 설치 스테이션 리스트
    cnt = here = 0 # 충전횟수 cnt, 지금위치 here
        
    while here + K < N: # 현재 있는 곳 + 이동거리 < 종착점일 때
        for move in range(K, 0, -1): # 최대 거리부터 알아보기 < 여기 생각못함
            if here + move in charge: # 만약 이동했을 때 충전기가 있다면
                here += move # 현장소에서 move만큼 이동
                cnt += 1 # 충전횟수 + 1
                break
        else: 
            cnt = 0
            break
    print(f'#{tc} {cnt}') # 테스트 케이스와 충전횟수 출력