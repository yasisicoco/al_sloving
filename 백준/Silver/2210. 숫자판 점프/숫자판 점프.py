import sys
sys.setrecursionlimit(10 ** 6)

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

def recur(si, sj):
    global check, check_lst

    if len(check) == 6: # 길이가 6인 문자열이 됐을 때
        if check not in check_lst: # 같은게 안에 없다면
            check_lst.append(check) # 추가 하고 돌아가기
            return
        else: # 같은게 안에 있다면
            return # 그냥 돌아감
    
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]

        if 0 <= ni < 5 and 0 <= nj < 5:
            check += str(arr[ni][nj])
            recur(ni, nj)
            check = check[:-1]

# 다섯개의 줄에 다섯 개의 정수로 숫자판.
arr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
check_lst = []
for i in range(5):
    check = ''
    for j in range(5):
        check += str(arr[i][j]) # 첫 값을 문자열로 바꿔서 넣어두기
        recur(i, j)
        if cnt <= len(check_lst): 
            cnt = len(check_lst)
        check = ''
print(cnt)