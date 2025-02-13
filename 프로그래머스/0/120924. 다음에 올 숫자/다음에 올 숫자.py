def solution(common):
    prev = common[0]
    median = common[1]
    nxt = common[2]
    
    result = 0
    if (nxt - median) == (median - prev):
        result = common[-1] + (median - prev)
    else:
        result = common[-1] * (median // prev)    
    return result