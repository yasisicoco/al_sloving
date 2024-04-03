N, need = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

# lst[0] : 국가번호
# lst[1] : 금
# lst[2] : 은
# lst[3] : 동
# print(lst)
lst.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)
# print(lst)
for k in range(N):
    if need == lst[k][0]:
        ans = k

# 만약 금메달 수가 같으면, 은메달 수를 확인
# 은메달 수도 같으면, 동메달 수를 확인
# 동메달도 같다면 앞 등수와 같은 등수 추가
# 그 다음 등수는 len(arr)의 등수로 추가

arr = []
cnt = 1
for i in range(N-1):
    if lst[i][1] == lst[i+1][1] and \
        lst[i][2] == lst[i+1][2] and \
        lst[i][3] == lst[i+1][3]:
        arr.append(cnt)

    else:
        arr.append(cnt)
        cnt += arr.count(cnt)
arr.append(cnt)

for j in range(N):
    if j == ans:
        print(arr[j])