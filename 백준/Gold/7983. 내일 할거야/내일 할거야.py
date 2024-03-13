import sys
input = sys.stdin.readline

N = int(input())

work = []
for _ in range(N):
    a, b = map(int, input().split())
    work.append((a, b)) # [][0]: 걸리는 날짜 / [][1]: 해당 과제 마지막 날

work.sort(key = lambda x: x[1], reverse=True)

days_left = work[0][1] - work[0][0] # 제일 마지막에 할 과제하고 남은 날

for i in range(1, len(work)):
    if days_left >= work[i][1]:
        days_left = work[i][1] - work[i][0]
    else: # days_left < work[i][1]
        days_left = days_left - work[i][0]
print(days_left)