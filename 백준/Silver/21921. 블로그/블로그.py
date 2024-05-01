# X일 동안 가장 많이 들어온 <방문자수, 기간>
# 블로그를 시작하고 지난 일수 N, X일 동안 가장 많이 들어옴
N, X = map(int, input().split())
arr = list(map(int, input().split()))
# X일 동안의 최대값을 구해야한다.
# 1. for문으로 전부 다 비교하면서 갱신?
# 2. dp 리스트를 만들어서 최대값만 반환? O(n)
dp = sum(arr[:X])

sumone = dp
cnt = 1
for i in range(1, N-X+1):
    dp = dp - arr[i-1] + arr[i+X-1]
    
    if sumone < dp:
        sumone = dp
        cnt = 1
    elif dp == sumone:
        cnt += 1

if dp == 0:
    print('SAD')
    exit()
else:
    print(sumone)
    print(cnt)