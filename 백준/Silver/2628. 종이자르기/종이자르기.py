row = [0] 
col = [0] 
r, c = map(int, input().split())
row.append(r)
col.append(c)
# 잘라야 하는 점선의 개수
M = int(input())

# M번 자르기
for i in range(M):
    # case: 0 > 가로줄자르는선(col이랑 비교) , case: 1 > 세로줄자르는선(row이랑 비교)
    case, num = map(int, input().split())
    if case == 0:
        col.append(num)
    if case == 1:
        row.append(num)
        
row.sort() # 오름차순정렬
col.sort()

ans_row = 0
for k in range(len(row)):
    if 0 <= k+1 < len(row):
        row_max_val = row[k+1] - row[k]
        if ans_row <= row_max_val:
            ans_row = row_max_val

ans_col = 0
for j in range(len(col)):
    if 0 <= j+1 < len(col):
        col_max_val = col[j+1] - col[j]
        if ans_col <= col_max_val:
            ans_col = col_max_val

result = ans_row * ans_col
print(result)