while True:
    try:
        N = int(input())
        st = ['-'] * (3**N)
        num = len(st)+1 // 3
        for i in range(1, (len(st)+1)):
            if i == num * 1: # 첫번째 지우는 라인
                pass
            elif i == num * 2: # 여기까지 지움
                st[i-1:num*2-1] = ' ' # 공백으로채움
    except: 
        break