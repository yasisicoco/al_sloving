import sys
sys.setrecursionlimit(10**6)

def work(start, sumone):
    global result
    if start > N: # 넘어가면 그냥리턴
        return
    
    if start == N:
        result = sumone

    if start <= N:
        result = sumone
    
    for j in range(start, N):
        if N < lst[j][0] + j:
            break
        sumone += lst[j][1]
        # print(sumone)
        work(lst[j][0] + j, sumone)
        
        
N = int(input())

lst = []
for m in range(N):
    t, p = map(int, input().split())
    lst.append((t, p))

# print(lst)

result = 0
ans = 0
for i in range(N): # 첫 근무
    if N < lst[i][0] + i:
        break
    sumone = lst[i][1]
    work(lst[i][0] + i, sumone) # 인덱스 볼 곳 / 더하는 값
    if ans <= result:
        ans = result

print(ans)
