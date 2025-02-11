
def solution(num, total):
    q = []
    for i in range(-1001, 1001):
        q.append(i)
        if len(q) == num:
            if sum(q) == total:
                break
            else:
                q.pop(0)
        
    return q

