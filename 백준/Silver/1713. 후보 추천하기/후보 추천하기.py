# 1713 후보 추천하기
# state 1

import sys
input = sys.stdin.readline

N = int(input())
R = int(input())
arr = list(map(int, input().split()))

lst = {}
for i in range(R):
    if arr[i] in lst: # 사진을 걸 곳에 이미 있는 경우
        lst[arr[i]][0] += 1 # 추천수 + 1
    else: # 사진거는곳에 없는 경우
        if len(lst) < N: # 사진거는 곳에 자리가 있다면
            lst[arr[i]] = [1, i] # 추천수 1, 들어온 순서 i
        else: # 자리가 없다면
            # lst의 요소들을 x[1][0]의 값의 오름차순으로 정렬하고, 같은 경우에는 x[1][1]의 값의 오름차순으로 정렬
            del_lst = sorted(lst.items(), key = lambda x : (x[1][0], x[1][1]))
            del(lst[del_lst[0][0]]) # 맨 앞을 제거
            lst[arr[i]] = [1, i] # 새로운 값 추가
            
result = list(sorted(lst.keys()))
print(*result)