N, S = map(int, input().split())
lst = list(map(int, input().split()))

def back(s, sumone):
    global cnt 

    if s == N:
        if sumone == S:
            cnt += 1
        return

    back(s+1, sumone+lst[s])
    back(s+1, sumone)

cnt = 0
back(0, 0)
if S == 0:
    cnt -= 1
print(cnt)