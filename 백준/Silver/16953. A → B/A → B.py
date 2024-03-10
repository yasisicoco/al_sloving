import sys
sys.setrecursionlimit(10**6)

def recur(num, cnt):
    global ans, cnt2
    
    if num == B:
        ans = B
        cnt2 = cnt
        return cnt
    if num > B:
        return cnt

    double(num, cnt)
    front_one(num, cnt)

def double(num, cnt):
    global ans
    if num == B:
        ans = B
        return cnt
    if num > B:
        return cnt
    
    num = num * 2
    cnt += 1
    recur(num, cnt)

def front_one(num, cnt):
    global ans
    if num == B:
        ans = B
        return cnt
    if num > B:
        return cnt
    
    num = str(num) + '1' # 앞에 1을 붙임
    num = int(num) # 정수로 변환
    cnt += 1
    recur(num, cnt)

ans = -1
cnt2= 0
A, B = map(int, input().split())
result = recur(A, 1)
if ans == B:
    print(cnt2)
else:
    print(ans)