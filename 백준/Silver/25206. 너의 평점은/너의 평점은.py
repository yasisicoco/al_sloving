# 전공평점은 전공과목별 (학점 * 과목평점) 의 합을 학점의 총합으로 나눈 값

# 평점
sum = 0
# 학점총합
rat_sum = 0
for i in range(20):
    sub = input().split()

    # 학점*평점
    avg = 0

    # 학점
    rat = float(sub[1])
    # 등급
    if sub[2]=='P':
        continue
    elif sub[2] == 'A+':
        avg = rat*4.5
    elif sub[2] == 'A0':
        avg = rat*4.0
    elif sub[2] == 'B+':
        avg = rat*3.5
    elif sub[2] == 'B0':
        avg = rat*3.0
    elif sub[2] == 'C+':
        avg = rat*2.5
    elif sub[2] == 'C0':
        avg = rat*2.0
    elif sub[2] == 'D+':
        avg = rat*1.5
    elif sub[2] == 'D0':
        avg = rat*1.0
    elif sub[2] == 'F':
        avg = rat*0

    rat_sum += rat
    sum += avg

# 전공평점
result = sum / rat_sum
print(result)