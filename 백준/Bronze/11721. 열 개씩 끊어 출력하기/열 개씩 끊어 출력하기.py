N = input() # 주어진 단어 str
K = len(N) # 주어진 단어 길이
text = [] # 빈 리스트

while True:
    if K == 0: # 주어진 단어 소진 시 그냥 출력 후 종료
        print(''.join(text)) 
        break
    for i in N:
        text.append(i) # 빈 리스트에 단어 한개씩 넣기
        if len(text) == 10: # 단어 10개 채워질때마다 출력
            print(''.join(text))
            text = [] # 리스트 초기화
        K -= 1 # 단어길이 줄이기