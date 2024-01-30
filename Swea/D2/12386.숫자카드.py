T = int(input())
for tc in range(1, T + 1): # 테스트 케이스
    N = int(input()) # 카드 장수
    dex = [0] * 10 # 인덱스 0부터 9까지 리스트로 생성
    ai = input() # str로 숫자받음
    new_ai = [] # ai 를 int 로 바꿔서 넣어줄 리스트
    for k in ai:
        int_k = int(k)
        new_ai.append(int_k)
    for i in new_ai:
        dex[i] += 1 # 인덱스 번호와 맞는 숫자 +1
 
    '''인덱스(dex) 생성완료
    0 1 2 3 4 5 6 7 8 9
    0 0 0 0 1 0 1 1 0 2
    '''
     
    max_ai = dex[0] # 인덱스에서 많이나온 수의 갯수
    max_idx = 0 # 인덱스에서 많이나온 수
 
    for j in range(1, len(dex)):
        if max_ai <= dex[j]: # 만약 많이 나온 수의 갯수가 같다면 큰 수를 선택 / 인덱스는 뒤로 갈수록 수가 커지므로 for문에 <= 를 쓰면 큰 수가 선택됨
            max_ai = dex[j]
            max_idx = j # 인덱스에서 많이 나온 수의 인덱스 번호
    print(f'#{tc} {max_idx} {max_ai}')