N = int(input())
ingre = []
for _ in range(N):
    ingre.append(list(map(int, input().split())))

result = 9999999999

def cook(i, sin, sun):
    global result
    if i == N:
        if sin != 1 or sun != 0:  # 재료 최소 1개 선택
            result = min(result, abs(sin-sun))
        return
    
    cook(i+1, sin*ingre[i][0], sun+ingre[i][1])
    cook(i+1, sin, sun)

cook(0, 1, 0)
print(result)