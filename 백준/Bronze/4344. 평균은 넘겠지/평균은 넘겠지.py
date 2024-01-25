C = int(input())

for i in range(C):
    num = list(map(int, input().split())) # 점수갯수와 점수값 받기
    numK = num.pop(0) # numK 에 점수갯수 반환
    number = 0 # 총점수 저장 변수
    aver_num = 0 # 평균점수를 넘는 점수갯수 저장 변수
    for j in num:
        number += j # 총점수 계산
    sum_number = number / numK # sum_number에 평균값 계산
    for k in num:
        if k > sum_number: # 평균값보다 높은 점수 구분
            aver_num += 1 # aver_num에 평균값보다 높은 점수 갯수 저장
    
    result = aver_num / numK * 100 # 평균값보다 높은점수갯수 / 원래 점수갯수
    print('{0:.3f}%'.format(result)) # 포맷함수를 통해 소수점 셋째자리까지 표현
