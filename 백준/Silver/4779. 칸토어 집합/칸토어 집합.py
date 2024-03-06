# 3**3 이면 길이가 27이고 인덱스가 0~26인 문자열
# 가운데 문자열을 공백
# 남은 두선의 가운데 문자열을 공백

# 시작점 + 끝점//3 = 첫번째 구간끝점 
# -------공백문자 넣을 공간-------
# 시작점 + (끝점//3)*2 = 두번째 구간 시작점

# 반복 > 문자열의 길이가 1이 되면 멈춤

def recur(start, end):
    if end == 1:
        return
    
    for i in range(start + end//3, start + (end//3)*2): # 중간지점
        st[i] = ' '
    recur(start, end//3) # 시작점부터 1/3 지점까지
    recur(start + (end//3)*2, end//3) # 2/3 지점부터 끝까지

while True:
    try:
        N = int(input())
        st = ['-'] * (3**N)
        recur(0, 3**N)
        print(*st, sep='')
    except EOFError: 
        break