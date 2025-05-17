def solution(citations):
    # 발표한 논문 n개
    n = len(citations)
    citations.sort(reverse=True)
    
    hIndex = 0
    for h in range(n+1): # 6 5 3 1 0
        cnt = 0
        for j in range(n):
            if citations[j] >= h:
                cnt += 1
        if cnt >= h:
            hIndex = max(h, hIndex)
        print(hIndex)
    return hIndex
