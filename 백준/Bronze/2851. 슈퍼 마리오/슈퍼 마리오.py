sumone = 0
for i in range(10):
    before_sumone = sumone # 더하기 전 값 저장
    sumone += int(input()) # 받아서 더함
    if sumone == 100:
        print(sumone)
        break
    if sumone > 100:
        if abs(100 - before_sumone) >= abs(sumone - 100):
            print(sumone)
            break
        else:
            print(before_sumone)
            break
if sumone < 100:
    print(sumone)