def solution(A, B):
    cnt = 0
    leng = len(A)
    flag = False
    while cnt < leng:
        if A == B:
            flag = True
            break
        
        # 회전 1회
        temp = A[-1]
        A = temp + A[:leng-1]
        cnt += 1
    
    if flag:
        return cnt
    else:
        return -1