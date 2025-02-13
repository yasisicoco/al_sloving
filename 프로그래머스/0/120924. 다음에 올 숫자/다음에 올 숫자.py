def solution(common):
    prev = common[0]
    median = common[1]
    nxt = common[2]
    
    result = 0
    cal = median - prev
    if (nxt - median) == (median - prev):
        result = common[-1] + cal
    else:
        cal = median // prev
        result = common[-1] * cal
    print(result)
    
    return result