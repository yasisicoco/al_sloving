N = int(input())

lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
    
cnt = 0
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i-1]: # 레벨 높은것보다 아래 레벨이 높을 때
        while True: # 1차이날 때까지
            if lst[i] == lst[i-1] - 1:
                break
            lst[i-1] = lst[i-1] - 1
            cnt += 1
print(cnt)