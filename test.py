from collections import deque

N = int(input())
arr = list(map(int, input().split()))
calc = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
# 연산횟수 add * sub * mul * div // 중복값 곱한거

q = deque(arr)
ans = q.popleft()
def dfs():
#     if add == 0 and sub == 0 and mul == 0 and div == 0:
#         max_val = max(ans, max_val)
#         min_val = min(ans, min_val)
    
    for i in range(4):
        if calc[i] == 0:
            continue
        
        
        if i == 0: #add
            calc[i] -= 1
            k = q.popleft()
            ans = ans + k
            dfs()
        elif i == 1: #sub
            calc[i] -= 1
            k = q.popleft()
            ans = ans - k
            dfs()
        elif i == 2: #mul
            calc[i] -= 1
            k = q.popleft()
            ans = ans * k
        elif i == 3: #div
            calc[i] -= 1
            k = q.popleft()
            if ans < 0: # 음수이면
                ans = abs(ans) // k # 양수로 바꾼뒤 몫을 취하고
                ans = -ans # 다시 음수로
            else:
                ans = ans // k
            dfs()
    pass
print(ans)