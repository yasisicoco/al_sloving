N = int(input())
upto = list(map(int, input().split()))


cnt = 0
result = 0
# ans = 0
for i in range(N):
    if 0 <= i+1 < N:
        if upto[i] < upto[i+1]: # 오르막이면
            cnt += (upto[i+1]-upto[i])
        elif upto[i] >= upto[i+1]: # 내리막이거나 같을 때
            if result <= cnt: # 올라온 길의값이 저장값보다 크면
                result = cnt # 값을 저장
                # ans = result # 다른곳에 저장
                cnt = 0   # 초기화
            else:
                cnt = 0
if result <= cnt:
    result = cnt
print(result)
