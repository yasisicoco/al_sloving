N, M = map(int, input().split())
S = []
for _ in range(N): # N 번의 반복
    str1 = input() # 동안 문자열 한개씩
    S.append(str1) # 집합 S에 추가

cnt = 0 # 집합 S에 포함된 문자열의 갯수
for _ in range(M):
    str2 = input()
    if str2 in S:
        cnt += 1
print(cnt)