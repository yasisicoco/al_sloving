# 빙고판
arr = [list(map(int, input().split())) for _ in range(5)]   
# 빙고 체크 
check = []
for _ in range(5):
    check += map(int, input().split())

bing = [0] * 26
for i in range(5):
    for j in range(5):
        bing[arr[i][j]] = (i, j)
        
v = [[0] * 10 for _ in range(4)]

for num in check:
    i, j = bing[num]
    v[0][j] += 1 # 세로
    v[1][i] += 1 # 가로
    v[2][i-j] += 1 # 오른쪽아래
    v[3][i+j] += 1 # 오른쪽 위
    cnt = 0
    for result in v:
        cnt += result.count(5)
    if cnt >= 3:
        break
print(sum(v[0]))