C = int(input())

for i in range(C):
    num = list(map(int, input().split()))
    numK = num.pop(0)
    number = 0
    aver_num = 0
    for j in num:
        number += j
    sum_number = number / numK
    for k in num:
        if k > sum_number:
            aver_num += 1
    
    result = aver_num / numK * 100
    print('{0:.3f}%'.format(result))