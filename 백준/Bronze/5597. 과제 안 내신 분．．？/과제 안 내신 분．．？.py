lst = [] # 빈 리스트
for i in range(1, 31): # 1부터 31까지 반복
    lst.append(i) # 1부터 31까지 lst에 추가
for _ in range(1, 29): # 28번 반복
    K = int(input()) # K에 입력값 할당
    lst.remove(K) # lst에 입력받은 K 삭제
print(min(lst)) # 남은 lst 의 최솟값
print(max(lst)) # 남은 lst 의 최댓값