N = int(input())

lst = []
for m in range(N):
    t, p = map(int, input().split())
    lst.append((t, p))

# print(lst)

result = 0
for i in range(N-1):
    day = lst[i][0] # 0: 일수, 1: 수입
    sumone = lst[i][1]
    for j in range(day+1, N):
        day += lst[j][0] # 0: 일수, 1: 수입
        sumone += lst[j][1]
        if day > N: # 근무일수가 지났으면
            day -= lst[j][0] # 전 근무일수 빼고 다시진행
            sumone -= lst[j][1]
            continue
        else: # 근무일수가 안지났으면 지금까지 더한 수익을 result와 비교 후 갱신
            if result <= sumone:
                result = sumone

print(result)