import sys
sys.setrecursionlimit(10**6)

def work(start, sumone):
    global result

    if start > N+1: # 넘어가면 그냥리턴
        return
    
    if start == N+1:
        result = max(sumone, result)
        return

    work(start + lst[start][0], sumone + lst[start][1])
    work(start + 1, sumone)
        
        
N = int(input())

lst = []
for m in range(N):
    t, p = map(int, input().split())
    lst.append((t, p))
    
lst = [0] + lst

result = 0
sumone = 0
work(1, sumone) # 인덱스 볼 곳 / 더하는 값

print(result)