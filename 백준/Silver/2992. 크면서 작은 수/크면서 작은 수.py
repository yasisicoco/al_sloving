def back(idx, current):
    if idx == len(strX):
        num = int(current)
        if num > X:
            result.append(num)
        return
    
    for i in range(len(strX)):
        if vis[i]:
            continue
        # 방문 표시
        vis[i] = True
        # 현재 숫자에 추가
        back(idx + 1, current + strX[i])
        # 방문 표시 해제
        vis[i] = False

result = []
X = int(input())
strX = str(X)
vis = [False] * len(strX)
back(0, "")

if not result:
    print(0)
else:
    print(min(result))
